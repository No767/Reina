import asyncio
import os

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
        # for items in self.bot.walk_application_commands():
        #     await helpUtils.addToHelpDB(
        #         uuid=str(uuid.uuid4()),
        #         name=items.qualified_name,
        #         parent_name=str(items.parent) if str(items.parent) is not None else "None",
        #         description=items.description,
        #         module=items.module,
        #         uri=HELP_CONNECTION_URI
        #     )
        mainPages = pages.Paginator(
            pages=[
                discord.Embed(description=f"[{str(items.parent)}]")
                for items in self.bot.walk_application_commands()
            ],
            loop_pages=True,
        )
        # mainPages = pages.Paginator(pages=[
        # discord.Embed(description=str(items.module))
        # for items in self.bot.walk_application_commands()
        # ], loop_pages=True)
        # await ctx.defer()
        await mainPages.respond(ctx.interaction, ephemeral=False)

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
                "AniList",
                "DisQuest",
                "Events",
                "Fun-Stuff",
                "GWS",
                "Jisho",
                "MangaDex",
                "MyAnimeList",
                "Tenor",
                "Useful-Things",
                "Waifu",
            ],
            required=False,
        ),
    ):
        if filters is None:
            await ctx.respond("sections")
        else:
            moduleType = str(filters).lower().strip()
            fullModule = f"Cogs.{moduleType}"
            mainRes = await helpUtils.getCmdsFromModule(
                module=fullModule, uri=HELP_CONNECTION_URI
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
