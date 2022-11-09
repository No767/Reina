import asyncio
import uuid

import discord
import uvloop
from dateutil import parser
from reina_events import ReinaEvents, ReinaEventsContextManager


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
        async with ReinaEventsContextManager(uri=self.uri, models=self.models):
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
        async with ReinaEventsContextManager(uri=self.uri, models=self.models):
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
