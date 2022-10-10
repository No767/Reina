import asyncio
import os
import uuid
from datetime import datetime, timezone

import discord
import uvloop
from dateutil import parser
from dateutil.relativedelta import relativedelta
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands, pages
from dotenv import load_dotenv
from reina_events import ReinaEvents, ReinaEventsUtils
from rin_exceptions import ItemNotFound, NoItemsError
from tortoise import Tortoise

load_dotenv()

POSTGRES_PASSWORD = os.getenv("Postgres_Password")
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_DATABASE = os.getenv("Postgres_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
CONNECTION_URI = f"asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"


eventUtils = ReinaEventsUtils(uri=CONNECTION_URI, models=["reina_events.models"])


class PurgeAllUserEventsView(discord.ui.View):
    async def on_timeout(self):
        for child in self.children:
            child.disabled = True

    @discord.ui.button(
        label="Yes",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:check:314349398811475968>"),
    )
    async def button_callback(self, button, interaction):
        getAllUserEvents = await eventUtils.getAllUserEvents(
            user_id=interaction.user.id
        )
        try:
            if len(getAllUserEvents) == 0 or getAllUserEvents is None:
                raise NoItemsError
            else:
                await eventUtils.purgeAllUserEvents(user_id=interaction.user.id)
                await interaction.response.send_message(
                    "All events have been purged", ephemeral=True
                )
        except NoItemsError:
            await interaction.response.send_message(
                "There seems to be no events to delete. Cancelling action...",
                ephemeral=True,
            )

    @discord.ui.button(
        label="No",
        row=0,
        style=discord.ButtonStyle.primary,
        emoji=discord.PartialEmoji.from_str("<:xmark:314349398824058880>"),
    )
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message(
            f"The action has been cancelled by the user {interaction.user.name}",
            ephemeral=True,
        )


class ReinaEventsCmds(commands.Cog):
    """Reina's Events - Allows you to set custom events and reminders"""

    def __init__(self, bot):
        self.bot = bot

    events = SlashCommandGroup(
        "reina-events",
        "Commands for Reina's Events system",
        guild_ids=[1006845509857714277],
    )
    eventsView = events.create_subgroup(
        "view", "View your events", guild_ids=[1006845509857714277]
    )
    eventsDelete = events.create_subgroup(
        "delete", "Delete your events", guild_ids=[1006845509857714277]
    )

    @events.command(name="create")
    async def eventCreate(
        self,
        ctx,
        *,
        name: Option(str, "The name of the event"),
        description: Option(str, "The description of the event"),
        date: Option(str, "The date of the event"),
        time: Option(str, "The time of the event"),
    ):
        """Creates an event"""
        currentDatetime = datetime.utcnow()
        eventDatetime = parser.parse(f"{date} {time}")
        await eventUtils.addEvent(
            uuid=uuid.uuid4(),
            user_id=ctx.author.id,
            name=name,
            description=description,
            date_added=currentDatetime,
            event_date=eventDatetime,
            event_passed=False,
        )
        await ctx.respond(f"Event {name} has been created")

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @eventsView.command(name="all")
    async def eventViewAll(self, ctx):
        """Views all of your events"""
        events = await eventUtils.getAllUserEvents(user_id=ctx.author.id)
        try:
            if len(events) == 0 or events is None:
                raise NoItemsError
            else:
                mainPages = pages.Paginator(
                    pages=[
                        discord.Embed(
                            title=item["name"], description=item["description"]
                        )
                        .add_field(
                            name="Date Added",
                            value=item["date_added"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(
                            name="Event Date",
                            value=item["event_date"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(name="Event Passed", value=item["event_passed"])
                        for item in events
                    ],
                    loop_pages=True,
                )
                await mainPages.respond(ctx.interaction, ephemeral=False)
        except NoItemsError:
            embedError = discord.Embed()
            embedError.description = "It seems like you don't have any events so far. Please create one to start seeing them here"
            await ctx.respond(embed=embedError)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @eventsView.command(name="past")
    async def eventViewPassed(self, ctx):
        """Views all of your past events"""
        events = await eventUtils.getUserEventPassedStatus(
            user_id=ctx.author.id, event_passed=True
        )
        try:
            if len(events) == 0 or events is None:
                raise NoItemsError
            else:
                mainPages = pages.Paginator(
                    pages=[
                        discord.Embed(
                            title=item["name"], description=item["description"]
                        )
                        .add_field(
                            name="Date Added",
                            value=item["date_added"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(
                            name="Event Date",
                            value=item["event_date"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(name="Event Passed", value=item["event_passed"])
                        for item in events
                    ],
                    loop_pages=True,
                )
                await mainPages.respond(ctx.interaction, ephemeral=False)
        except NoItemsError:
            embedError = discord.Embed()
            embedError.description = "It seems like you don't have any events so far. Please create one to start seeing them here"
            await ctx.respond(embed=embedError)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @eventsView.command(name="upcoming")
    async def eventViewUpcoming(self, ctx):
        """Views all of your upcoming events"""
        events = await eventUtils.getUserEventPassedStatus(
            user_id=ctx.author.id, event_passed=False
        )
        try:
            if len(events) == 0 or events is None:
                raise NoItemsError
            else:
                mainPages = pages.Paginator(
                    pages=[
                        discord.Embed(
                            title=item["name"], description=item["description"]
                        )
                        .add_field(
                            name="Date Added",
                            value=item["date_added"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(
                            name="Event Date",
                            value=item["event_date"].strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        .add_field(name="Event Passed", value=item["event_passed"])
                        for item in events
                    ],
                    loop_pages=True,
                )
                await mainPages.respond(ctx.interaction, ephemeral=False)
        except NoItemsError:
            embedError = discord.Embed()
            embedError.description = "It seems like you don't have any events so far or all of the events that you have passed. Please create one to start seeing them here"
            await ctx.respond(embed=embedError)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    # Later on this should use a modal just to be secure
    @eventsDelete.command(name="one")
    async def eventDeleteOne(self, ctx, *, name: Option(str, "The name of the event")):
        """Deletes an event belonging to the user"""
        eventData = await eventUtils.getFirstUserEventsName(
            user_id=ctx.author.id, name=name
        )
        try:
            if eventData is None:
                raise NoItemsError
            else:
                await ReinaEvents.filter(name=name, user_id=ctx.author.id).delete()
                embedSuccess = discord.Embed()
                embedSuccess.description = f"Successfully deleted the event {name}"
                await ctx.respond(embed=embedSuccess, ephemeral=True)
        except ItemNotFound:
            embedError = discord.Embed()
            embedError.description = (
                f"No items could be found with the name {name}. Please try again"
            )
            await ctx.respond(embedError, ephemeral=True)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @eventsDelete.command(name="all")
    async def eventDeleteAll(self, ctx):
        """Deletes all of the events that a user has"""
        embed = discord.Embed()
        embed.description = "Are you sure you want to delete all of your events? This action cannot be undone"
        await ctx.respond(embed=embed, view=PurgeAllUserEventsView(), ephemeral=True)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @eventsView.command(name="countdown")
    async def eventCountdown(self, ctx, *, name: Option(str, "The name of the event")):
        """Checks how much days until an event will happen and pass"""
        eventData = await eventUtils.getFirstUserEventsName(
            user_id=ctx.author.id, name=name
        )
        try:
            if eventData is None:
                raise ItemNotFound
            else:
                embed = discord.Embed()
                timeDiff = eventData["event_date"] - datetime.now(timezone.utc)
                rdelta = relativedelta(
                    datetime.now(timezone.utc), eventData["event_date"]
                )
                countHours, rem = divmod(timeDiff.seconds, 3600)
                countMinutes, countSeconds = divmod(rem, 60)
                embed.description = f"{name} will happen in {rdelta.years} year(s), {timeDiff.days} day(s), {countHours} hour(s), {countMinutes} minute(s), and {countSeconds} second(s)"
                embed.add_field(
                    name="Event Date",
                    value=eventData["event_date"].strftime("%Y-%m-%d %H:%M:%S"),
                )
                embed.add_field(
                    name="Today's Date",
                    value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
                await ctx.respond(embed=embed)
        except ItemNotFound:
            embedError = discord.Embed()
            embedError.description = (
                f"No items could be found with the name {name}. Please try again"
            )
            await ctx.respond(embed=embedError)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @events.command(name="update")
    async def eventUpdate(
        self,
        ctx,
        *,
        name: Option(str, "The event to update"),
        date: Option(str, "The new date of the event"),
        time: Option(str, "The nnew time of the event"),
    ):
        """Updates an event's date and time"""
        await Tortoise.init(
            db_url=CONNECTION_URI, modules={"models": ["reina_events.models"]}
        )
        parsedDate = parser.parse(f"{date} {time}")
        eventData = await eventUtils.getFirstUserEventsName(
            user_id=ctx.author.id, name=name
        )
        try:
            if eventData is None:
                raise ItemNotFound
            else:
                await ReinaEvents.filter(name=name, user_id=ctx.author.id).update(
                    event_date=parsedDate
                )
                await Tortoise.close_connections()
                embedSuccess = discord.Embed()
                embedSuccess.description = (
                    f"Successfully updated the event {name} to {parsedDate}"
                )
                await ctx.respond(embed=embedSuccess, ephemeral=True)
        except ItemNotFound:
            await Tortoise.close_connections()
            embedError = discord.Embed()
            embedError.description = (
                f"No items could be found with the name {name}. Please try again"
            )
            await ctx.respond(embedError, ephemeral=True)


def setup(bot):
    bot.add_cog(ReinaEventsCmds(bot))
