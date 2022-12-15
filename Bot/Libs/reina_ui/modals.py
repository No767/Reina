import asyncio
import uuid
from typing import List

import discord
import uvloop
from dateutil import parser
from reina_events import ReinaEvents
from reina_genshin_wish_sim import ReinaGWSCacheUtils, WSUserInv
from reina_utils import ReinaCM
from rin_exceptions import ItemNotFound


class DeleteOneEventModal(discord.ui.Modal):
    def __init__(self, uri: str, models: list, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models
        self.add_item(
            discord.ui.InputText(
                label="Event Name",
                placeholder="Event Name",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            doesEventExist = await ReinaEvents.filter(
                name=self.children[0].value, user_id=interaction.user.id
            ).first()
            if doesEventExist is not None:
                await ReinaEvents.filter(
                    name=self.children[0].value, user_id=interaction.user.id
                ).delete()
                await interaction.response.send_message(
                    content=f"Event {self.children[0].value} has been deleted",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    content=f"Event {self.children[0].value} does not exist",
                    ephemeral=True,
                )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class AddEventModal(discord.ui.Modal):
    def __init__(self, uri: str, models: list, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models
        self.add_item(
            discord.ui.InputText(
                label="Event Name",
                placeholder="Event Name",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="Event description",
                placeholder="Event desc",
                min_length=1,
                style=discord.InputTextStyle.long,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="Event Date",
                placeholder="Event Date",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="Event Time",
                placeholder="Event Time",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            currentDateTime = discord.utils.utcnow()
            eventDateTime = parser.parse(
                f"{self.children[2].value} {self.children[3].value}"
            )
            await ReinaEvents.create(
                uuid=str(uuid.uuid4()),
                user_id=interaction.user.id,
                name=self.children[0].value,
                description=self.children[1].value,
                date_added=currentDateTime,
                event_date=eventDateTime,
                event_passed=False,
            )
            await interaction.response.send_message(
                content=f"Event {self.children[0].value} has been created",
                ephemeral=True,
            )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class UpdateEventModal(discord.ui.Modal):
    def __init__(self, uri: str, models: list, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models
        self.add_item(
            discord.ui.InputText(
                label="Event Name",
                placeholder="The event to update",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="New Event Date",
                placeholder="The new event date to update to",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="New Event Time",
                placeholder="The new event time to update to",
                min_length=1,
                style=discord.InputTextStyle.short,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            newEventDatetime = parser.parse(
                f"{self.children[1].value} {self.children[2].value}"
            )
            try:
                getEvent = await ReinaEvents.filter(
                    name=self.children[0].value, user_id=interaction.user.id
                ).first()
                if getEvent is None:
                    raise ItemNotFound
                else:
                    await ReinaEvents.filter(
                        name=self.children[0].value, user_id=interaction.user.id
                    ).update(event_date=newEventDatetime)
                    await interaction.response.send_message(
                        f"Event {self.children[0].value} has been updated to {discord.utils.format_dt(newEventDatetime, style='F')}",
                        ephemeral=True,
                    )
            except ItemNotFound:
                await interaction.response.send_message(
                    f"Event {self.children[0].value} does not exist", ephemeral=True
                )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class GWSDeleteOneUserInvItemModal(discord.ui.Modal):
    def __init__(
        self,
        uri: str,
        models: List,
        redis_host: str,
        redis_port: int,
        command_name: str,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.command_name = command_name
        self.cache = ReinaGWSCacheUtils(
            uri=self.uri,
            models=self.models,
            redis_host=self.redis_host,
            redis_port=self.redis_port,
        )
        self.add_item(
            discord.ui.InputText(
                label="Name",
                placeholder="Type in the item name to delete",
                min_length=1,
                max_length=255,
                required=True,
                style=discord.InputTextStyle.short,
            )
        )
        self.add_item(
            discord.ui.InputText(
                label="Amount",
                placeholder="Type in the item amount to delete",
                min_length=1,
                max_length=255,
                required=True,
                style=discord.InputTextStyle.short,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            userInvItem = await self.cache.cacheUserInvItem(
                user_id=interaction.user.id,
                name=self.children[0].value,
                command_name=self.command_name,
            )
            if userInvItem is None:
                return await interaction.response.send_message(
                    f"The item ({self.children[0].value}) could not be found. Please try again",
                    ephemeral=True,
                )
            elif int(self.children[1].value) > userInvItem["amount"]:
                return await interaction.response.send_message(
                    f"The amount requested ({self.children[1].value}) is more than the amount you have ({userInvItem['amount']}). Please try again",
                    ephemeral=True,
                )
            else:
                await WSUserInv.filter(
                    user_id=interaction.user.id, name=userInvItem["name"]
                ).update(amount=userInvItem["amount"] - int(self.children[1].value))
                return await interaction.response.send_message(
                    f"Deleted {self.children[1].value} {self.children[0].value}(s) from your inventory",
                    ephemeral=True,
                )
