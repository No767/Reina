import asyncio
import datetime
import platform
import time

import discord
import uvloop
from discord.commands import SlashCommandGroup
from discord.ext import commands


class Reina(commands.Cog):
    """Commands for getting info about Reina"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    reina = SlashCommandGroup("reina", "Utility Commands for Reina")

    @reina.command(name="uptime")
    async def botUptime(self, ctx):
        """Returns Reina's Uptime"""
        uptime = datetime.timedelta(seconds=int(round(time.time() - startTime)))
        embed = discord.Embed(color=discord.Color.from_rgb(245, 227, 255))
        embed.description = f"Reina's Uptime: `{uptime.days} Days, {uptime.seconds//3600} Hours, {(uptime.seconds//60)%60} Minutes, {(uptime.seconds%60)} Seconds`"
        await ctx.respond(embed=embed)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @reina.command(name="version")
    async def version(self, ctx):
        """Returns Reina's Current Version"""
        embedVar = discord.Embed()
        embedVar.description = "Build Version: v2.5.0"
        await ctx.respond(embed=embedVar)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @reina.command(name="ping")
    async def pingChecker(self, ctx):
        """Returns Reina's Ping"""
        embed = discord.Embed()
        embed.description = f"Bot Latency: {round(self.bot.latency * 1000)}ms"
        await ctx.respond(embed=embed)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @reina.command(name="platform")
    async def reinaPlatform(self, ctx):
        """Returns platform info about Reina"""
        embed = discord.Embed(color=discord.Color.from_rgb(255, 201, 255))
        embed.title = "Platform Info"
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.add_field(
            name="Python Version", value=f"[{platform.python_version()}]", inline=True
        )
        embed.add_field(
            name="Python Compiler", value=f"[{platform.python_compiler()}]", inline=True
        )
        embed.add_field(
            name="Pycord Version", value=f"[{discord.__version__}]", inline=True
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Reina(bot))
