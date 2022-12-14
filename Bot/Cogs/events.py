import asyncio
import os
import sys
import urllib.parse
from pathlib import Path

import discord
import uvloop
from dateutil.relativedelta import relativedelta
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands, pages
from dotenv import load_dotenv
from reina_events import ReinaEvents
from reina_ui import (
    AddEventModal,
    DeleteOneEventModal,
    PurgeAllEventsView,
    UpdateEventModal,
)
from reina_utils import ReinaCM
from rin_exceptions import ItemNotFound, NoItemsError

path = Path(__file__).parents[1].absolute()
packagePath = os.path.join(str(path), "Libs")
envPath = os.path.join(str(path), ".env")
sys.path.append(packagePath)

load_dotenv()

POSTGRES_PASSWORD = urllib.parse.quote_plus(os.getenv("Postgres_Password"))
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_DATABASE = os.getenv("Postgres_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
CONNECTION_URI = f"asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"


class Events(commands.Cog):
    """Reina's Events - Allows you to set custom events"""

    def __init__(self, bot):
        self.bot = bot

    events = SlashCommandGroup(
        "events",
        "Commands for Reina's Events system",
    )
    eventsDelete = events.create_subgroup("delete", "Delete your events")

    @events.command(name="create")
    async def eventCreate(self, ctx):
        """Creates an event"""
        addModal = AddEventModal(
            uri=CONNECTION_URI, models=["reina_events.models"], title="Create an event"
        )
        await ctx.send_modal(addModal)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @events.command(name="view")
    async def viewEvents(
        self,
        ctx,
        *,
        filter: Option(
            str, "Filter the events by the type", choices=["All", "Upcoming", "Passing"]
        ),
    ):
        """Views events that you have"""
        async with ReinaCM(uri=CONNECTION_URI, models=["reina_events.models"]):
            events = await ReinaEvents.filter(user_id=ctx.user.id).all().values()
            if filter == "Upcoming":
                events = await ReinaEvents.filter(
                    user_id=ctx.user.id, event_passed=False
                ).values()
            elif filter == "Passed":
                events = await ReinaEvents.filter(
                    user_id=ctx.user.id, event_passed=True
                ).values()
            try:
                if len(events) == 0:
                    raise NoItemsError
                else:
                    mainPages = pages.Paginator(
                        pages=[
                            discord.Embed(
                                title=items["name"], description=items["description"]
                            )
                            .add_field(
                                name="Date Added (UTC)",
                                value=discord.utils.format_dt(
                                    items["date_added"], style="F"
                                ),
                            )
                            .add_field(
                                name="Event Date (UTC)",
                                value=discord.utils.format_dt(
                                    items["event_date"], style="F"
                                ),
                            )
                            .add_field(
                                name="Event Passed?", value=items["event_passed"]
                            )
                            for items in events
                        ],
                        loop_pages=True,
                    )
                    await mainPages.respond(ctx.interaction, ephemeral=False)
            except NoItemsError:
                embedError = discord.Embed()
                embedError.description = "It seems like you don't have any events so far. Please create one to start seeing them here"
                await ctx.respond(embed=embedError, ephemeral=True)

    @eventsDelete.command(name="one")
    async def eventDeleteOne(self, ctx):
        """Deletes an event belonging to the user"""
        deleteModal = DeleteOneEventModal(
            uri=CONNECTION_URI, models=["reina_events.models"], title="Delete a event"
        )
        await ctx.send_modal(deleteModal)

    @eventsDelete.command(name="all")
    async def eventDeleteAll(self, ctx):
        """Deletes all of the events that a user has"""
        embed = discord.Embed()
        embed.description = "Are you sure you want to delete all of your events? This action cannot be undone"
        await ctx.respond(
            embed=embed,
            view=PurgeAllEventsView(uri=CONNECTION_URI, models=["reina_events.models"]),
            ephemeral=True,
        )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @events.command(name="update")
    async def eventUpdate(
        self,
        ctx,
    ):
        """Updates an event's date and time"""
        updateModal = UpdateEventModal(
            uri=CONNECTION_URI, models=["reina_events.models"], title="Update a event"
        )
        await ctx.send_modal(updateModal)

    @events.command(name="countdown")
    async def eventCountdown(self, ctx, *, name: Option(str, "The name of the event")):
        """Checks how much days until an event will happen and pass"""
        async with ReinaCM(uri=CONNECTION_URI, models=["reina_events.models"]):
            eventData = (
                await ReinaEvents.filter(user_id=ctx.user.id, name=name)
                .first()
                .values()
            )
            try:
                if eventData is None:
                    raise ItemNotFound
                else:
                    embed = discord.Embed()
                    timeDiff = eventData["event_date"] - discord.utils.utcnow()
                    rdelta = relativedelta(
                        discord.utils.utcnow(), eventData["event_date"]
                    )
                    countHours, rem = divmod(timeDiff.seconds, 3600)
                    countMinutes, countSeconds = divmod(rem, 60)
                    embed.description = f"**{name}** will happen {discord.utils.format_dt(eventData['event_date'], style='R')} ({rdelta.years} year(s), {timeDiff.days} day(s), {countHours} hour(s), {countMinutes} minute(s), and {countSeconds} second(s))"
                    embed.add_field(
                        name="Event Date (UTC)",
                        value=discord.utils.format_dt(
                            eventData["event_date"], style="F"
                        ),
                    )
                    embed.add_field(
                        name="Today's Date (UTC)",
                        value=discord.utils.format_dt(
                            discord.utils.utcnow(), style="F"
                        ),
                    )
                    await ctx.respond(embed=embed)
            except ItemNotFound:
                embedError = discord.Embed()
                embedError.description = (
                    f"No items could be found with the name {name}. Please try again"
                )
                await ctx.respond(embed=embedError, ephemeral=True)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def setup(bot):
    bot.add_cog(Events(bot))
