import asyncio
from typing import List

import discord
import uvloop
from reina_events import ReinaEvents
from reina_genshin_wish_sim import WSUserInv
from reina_utils import ReinaCM
from rin_exceptions import NoItemsError


class PurgeAllEventsView(discord.ui.View):
    async def on_timeout(self):
        for child in self.children:
            child.disabled = True

    def __init__(self, uri: str, models: list, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models

    @discord.ui.button(
        label="Yes",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:check:314349398811475968>"),
    )
    async def button_callback(self, button, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            getUserEvent = await ReinaEvents.filter(user_id=interaction.user.id).first()
            try:
                if getUserEvent is None:
                    raise NoItemsError
                else:
                    await ReinaEvents.filter(user_id=interaction.user.id).delete()
                    for child in self.children:
                        child.disabled = True
                    await interaction.response.edit_message(
                        embed=discord.Embed(
                            description="All of your events have been purged"
                        ),
                        view=self,
                    )
            except NoItemsError:
                for child in self.children:
                    child.disabled = True
                await interaction.response.edit_message(
                    embed=discord.Embed(
                        description="There seems to be no events to delete... Cancelling action"
                    ),
                    view=self,
                )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @discord.ui.button(
        label="No",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:xmark:314349398824058880>"),
    )
    async def second_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(
            embed=discord.Embed(
                description=f"The action has been cancelled by the user {interaction.user.name}"
            ),
            view=self,
        )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class GWSPurgeInvView(discord.ui.View):
    async def on_timeout(self):
        for child in self.children:
            child.disabled = True

    def __init__(self, uri: str, models: List, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models

    @discord.ui.button(
        label="Yes",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:check:314349398811475968>"),
    )
    async def button_callback(self, button, interaction: discord.Interaction):
        async with ReinaCM(uri=self.uri, models=self.models):
            invExist = await WSUserInv.filter(user_id=interaction.user.id).exists()
            if invExist is False:
                for child in self.children:
                    child.disabled = True
                await interaction.response.edit_message(
                    embed=discord.Embed(
                        description="It seems like you don't have anything in your GWS inventory. Please try again"
                    ),
                    view=self,
                    delete_after=15.0,
                )
            else:
                await WSUserInv.filter(user_id=interaction.user.id).delete()
                for child in self.children:
                    child.disabled = True
                await interaction.response.edit_message(
                    embed=discord.Embed(
                        description="Everything has been purged from your inventory. This cannot be recovered from."
                    ),
                    view=self,
                    delete_after=15.0,
                )

    @discord.ui.button(
        label="No",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:xmark:314349398824058880>"),
    )
    async def second_button_callback(self, button, interaction: discord.Interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(
            embed=discord.Embed(
                description=f"This action has been canceled by {interaction.user.name}"
            ),
            view=self,
            delete_after=15.0,
        )
