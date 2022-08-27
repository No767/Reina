import asyncio
import os
import uuid

import discord
import uvloop
from discord.commands import Option, slash_command
from discord.ext import commands, pages
from dotenv import load_dotenv
from help_utils import ReinaHelpUtils

load_dotenv()

POSTGRES_PASSWORD = os.getenv("Postgres_Password")
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_HELP_DATABASE = os.getenv("Postgres_Help_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
HELP_CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_HELP_DATABASE}"

helpUtils = ReinaHelpUtils()


class SmarterHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="smarter-help",
        description="Another smarter help command",
        guild_ids=[1006845509857714277],
    )
    async def smarterHelp(self, ctx: discord.ApplicationContext):
        for items in self.bot.walk_application_commands():
            await helpUtils.addToHelpDB(
                uuid=str(uuid.uuid4()),
                name=items.qualified_name,
                parent_name=str(items.parent)
                if str(items.parent) is not None
                else "None",
                description=items.description,
                module=str(items.module).replace("Cogs.", ""),
                uri=HELP_CONNECTION_URI,
            )
        # mainPages = pages.Paginator(
        #     pages=[
        #         discord.Embed(description=f"[{str(items.parent)}]")
        #         for items in self.bot.walk_application_commands()
        #     ],
        #     loop_pages=True,
        # )
        # mainPages = pages.Paginator(pages=[
        # discord.Embed(description=str(items.qualified_name))
        # for items in self.bot.walk_application_commands()
        # ], loop_pages=True)
        await ctx.defer()
        await ctx.respond("help me")
        # await mainPages.respond(ctx.interaction, ephemeral=False)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @slash_command(
        name="help-main",
        description="mainly for testing the help system",
        guild_ids=[1006845509857714277],
    )
    async def evenSmarterHelp(
        self,
        ctx,
        *,
        filters: Option(
            str,
            "The filters to choose from",
            choices=[
                "All",
                "AniList",
                "DisQuest",
                "Events",
                "Fun",
                "GWS",
                "Jisho",
                "MangaDex",
                "MyAnimeList",
                "Reina",
                "Tenor",
                "Utility",
                "Waifu",
            ],
            required=False,
        ),
    ):
        if filters is None:
            embedMain = discord.Embed(color=discord.Color.from_rgb(255, 201, 255))
            embedMain.set_author(
                name=f"Help", icon_url=self.bot.user.display_avatar.url
            )
            embedMain.description = "Welcome! Reina is a fork of Beryl, which focuses on improving features of Beryl, and adding new ones as well. To check out the commands, check out the filters option for a section by section breakdown of the commands."
            await ctx.respond(embed=embedMain)
        elif filters in ["All"]:
            getAllCmds = await helpUtils.getAllCommands(uri=HELP_CONNECTION_URI)
            mainPages = pages.Paginator(
                pages=[
                    discord.Embed(
                        title=dict(mainItems)["name"],
                        description=dict(mainItems)["description"],
                    )
                    .add_field(
                        name="Parent Name",
                        value=dict(mainItems)["parent_name"],
                        inline=True,
                    )
                    .add_field(
                        name="Module", value=dict(mainItems)["module"], inline=True
                    )
                    for mainItems in getAllCmds
                ],
                loop_pages=True,
            )
            await mainPages.respond(ctx.interaction, ephemeral=False)
        else:
            moduleType = str(filters).lower().strip()
            mainRes = await helpUtils.getCmdsFromModule(
                module=moduleType, uri=HELP_CONNECTION_URI
            )
            embed = discord.Embed(color=discord.Color.from_rgb(255, 201, 255))
            embed.set_author(
                name=f"Help - {filters}", icon_url=self.bot.user.display_avatar.url
            )
            for items in mainRes:
                embed.add_field(
                    name=f"`{dict(items)['name']}`",
                    value=f"{dict(items)['description']}",
                    inline=True,
                )
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(SmarterHelp(bot))
