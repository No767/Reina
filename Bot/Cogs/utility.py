import asyncio
import datetime
import os
import time

import aiohttp
import discord
import ffmpeg
import orjson
import simdjson
import uvloop
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands

parser = simdjson.Parser()
hypixel_api_key = os.getenv("Hypixel_API_Key")


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    utils = SlashCommandGroup(
        "utils", "Util Commands for Reina", guild_ids=[1006845509857714277]
    )

    @utils.command(name="ffmpegcve")
    async def ffmpegcve(
        self,
        ctx,
        *,
        video_file: Option(discord.Attachment, "The file to convert to mp4"),
    ):
        """Converts video files to mp4"""
        try:
            await video_file.save(fp="video")
            await ctx.respond("converting to mp4...")
            ffmpeg.input("video").output("ffmpeg.mp4").run()
            os.system("rm video")
            await ctx.respond("sending...")
            await ctx.respond(file=discord.File(r"ffmpeg.mp4"))
        except Exception as e:
            embedError = discord.Embed()
            embedError.description = "Something went wrong. Please try again"
            embedError.add_field(name="Error", value=e, inline=True)
            await ctx.respond(embed=embedError)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @utils.command(name="ping")
    async def pingChecker(self, ctx):
        """Returns Reina's Ping"""
        embed = discord.Embed()
        embed.description = f"Bot Latency: {round(self.bot.latency * 1000)}ms"
        await ctx.respond(embed=embed)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @utils.command(name="hypixel-count")
    async def player_count(self, ctx):
        """Gets the amount of players in each game server"""
        async with aiohttp.ClientSession(json_serialize=orjson.dumps) as session:
            params = {"key": hypixel_api_key}
            async with session.get(
                "https://api.hypixel.net/counts", params=params
            ) as response:
                status = await response.content.read()
                statusMain = parser.parse(status, recursive=True)
                try:
                    embedVar = discord.Embed(
                        title="Games Player Count",
                        color=discord.Color.from_rgb(186, 193, 255),
                    )
                    for k, v in statusMain["games"].items():
                        embedVar.add_field(name=k, value=v["players"], inline=True)
                    await ctx.respond(embed=embedVar)
                except Exception as e:
                    embedVar = discord.Embed()
                    embedVar.description = "The command broke. Please try again."
                    embedVar.add_field(name="Reason", value=str(e), inline=False)
                    await ctx.respond(embed=embedVar)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @utils.command(name="uptime")
    async def botUptime(self, ctx):
        """Returns Reina's Uptime"""
        uptime = datetime.timedelta(seconds=int(round(time.time() - startTime)))
        embed = discord.Embed(color=discord.Color.from_rgb(245, 227, 255))
        embed.description = f"Reina's Uptime: `{uptime.days} Days, {uptime.seconds//3600} Hours, {(uptime.seconds//60)%60} Minutes, {(uptime.seconds%60)} Seconds`"
        await ctx.respond(embed=embed)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @utils.command(name="version")
    async def version(self, ctx):
        """Returns Reina's Current Version"""
        embedVar = discord.Embed()
        embedVar.description = "Build Version: v2.3.0"
        await ctx.respond(embed=embedVar)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def setup(bot):
    bot.add_cog(Utils(bot))
