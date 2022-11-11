import asyncio

import discord
import uvloop
from reina_events import ReinaEvents, ReinaEventsContextManager
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
        async with ReinaEventsContextManager(uri=self.uri, models=self.models):
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
