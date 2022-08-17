import discord
import discord.ext
from discord.commands import Option, slash_command
from discord.ext import commands


class ReinaHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    @slash_command(
        name="help",
        description="The help command for Reina",
    )
    async def reinaHelp(
        self,
        ctx,
        *,
        category: Option(
            str,
            "The different categories that Reina has",
            choices=[
                "AniList",
                "DisQuest",
                "Events",
                "Fun-Stuff",
                "Jisho",
                "MangaDex",
                "MyAnimeList",
                "Tenor",
                "Utility",
                "Waifu",
            ],
            required=False,
        )
    ):
        if category is None:
            bot = self.bot
            embed = discord.Embed(
                title="Help", color=discord.Color.from_rgb(255, 196, 253)
            )
            embed.add_field(name="AniList", value="`/help AniList`", inline=True)
            embed.add_field(name="DisQuest", value="`/help DisQuest`", inline=True)
            embed.add_field(name="Events", value="`/help Events`", inline=True)
            embed.add_field(name="Fun Stuff", value="`/help Fun-Stuff`", inline=True)
            embed.add_field(name="Jisho", value="`/help Jisho`", inline=True)
            embed.add_field(name="MangaDex", value="`/help MangaDex`", inline=True)
            embed.add_field(
                name="MyAnimeList", value="`/help MyAnimeList`", inline=True
            )
            embed.add_field(name="Tenor", value="`/help Tenor`", inline=True)
            embed.add_field(name="Utility", value="`/help Utility`", inline=True)
            embed.add_field(name="Waifu", value="`/help Waifu`", inline=True)
            embed.set_author(
                name="Help",
                url=discord.Embed.Empty,
                icon_url=bot.user.display_avatar,
            )
            embed.set_footer(text='Remember, the command prefix for this bot is "/"')
            await ctx.respond(embed=embed)

        if category in ["AniList"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `anilist`"
            embedVar.add_field(
                name="`search anime`",
                value="Searches up to 25 animes on AniList",
                inline=True,
            )
            embedVar.add_field(
                name="`search manga`",
                value="Searches up to 25 mangas on AniList",
                inline=True,
            )
            embedVar.add_field(
                name="`search tags`",
                value="Searches up to 25 tags on AniList",
                inline=True,
            )
            embedVar.add_field(
                name="`search users`",
                value="Searches up to 25 users on AniList",
                inline=True,
            )
            embedVar.add_field(
                name="`search characters`",
                value="Searches up to 25 characters on AniList",
                inline=True,
            )
            embedVar.add_field(
                name="`search actors`",
                value="Searches up to 25 actors on AniList",
                inline=True,
            )
            embedVar.set_author(name="Help - AniList", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)

        if category in ["DisQuest"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `disquest`"
            embedVar.add_field(
                name="`init`",
                value="initializes the account for DisQuest",
                inline=True,
            )
            embedVar.add_field(
                name="`mylvl`",
                value="Displays your current level",
                inline=True,
            )
            embedVar.add_field(
                name="`rank local`",
                value="Displays the most active members of your server",
                inline=True,
            )
            embedVar.add_field(
                name="`rank global`",
                value="Displays global rankings for DisQuest",
                inline=True,
            )
            embedVar.set_author(
                name="Help - DisQuest", icon_url=bot.user.display_avatar
            )
            await ctx.respond(embed=embedVar)

        if category in ["Events"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `events`"
            embedVar.add_field(
                name="`view all`",
                value="Views all of your past and upcoming events",
                inline=True,
            )
            embedVar.add_field(
                name="`create`",
                value="Creates a new event",
                inline=True,
            )
            embedVar.add_field(
                name="`delete all`",
                value="Purges all events from your user",
                inline=True,
            )
            embedVar.add_field(
                name="`delete one`",
                value="Deletes one event from your list of events",
                inline=True,
            )
            embedVar.add_field(
                name="`update`",
                value="Updates the date and time of an event",
                inline=True,
            )
            embedVar.add_field(
                name="`view countdown`",
                value="Checks how much days until an event will happen and pass",
                inline=True,
            )
            embedVar.add_field(
                name="`view past`",
                value="View all of your past events",
                inline=True,
            )
            embedVar.set_author(name="Help - Events", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)

        if category in ["Fun-Stuff"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.add_field(
                name="`ship`",
                value="Calculates how much love a person has",
                inline=True,
            )
            embedVar.add_field(
                name="`sex`",
                value="it's a sex calculator",
                inline=True,
            )
            embedVar.add_field(
                name="`laugh`",
                value="laughs",
                inline=True,
            )
            embedVar.add_field(
                name="`random_int`",
                value="Based on 2 limits, returns a random number",
                inline=True,
            )
            embedVar.set_author(
                name="Help - Fun Stuff", icon_url=bot.user.display_avatar
            )
            await ctx.respond(embed=embedVar)

        if category in ["Jisho"]:
            bot = self.bot
            embedVar = discord.Embed(color=14414079)
            embedVar.add_field(
                name="`jisho`",
                value="Searches for any words and/or definitions on Jisho",
                inline=True,
            )
            embedVar.set_author(name="Help - Jisho", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)

        if category in ["MangaDex"]:
            bot = self.bot
            embedVar = discord.Embed(color=14414079)
            embedVar.description = "Base command: `mangadex`"
            embedVar.add_field(
                name="`search scanlation`",
                value="Returns up to 5 scanlation groups via the name given",
                inline=True,
            )
            embedVar.add_field(
                name="`search manga`",
                value="Searches for up to 5 manga on MangaDex",
                inline=True,
            )
            embedVar.add_field(
                name="`search author`",
                value="Returns up to 5 authors and their info",
                inline=True,
            )
            embedVar.add_field(
                name="`random`",
                value="Returns an random manga from MangaDex",
                inline=True,
            )
            embedVar.set_author(
                name="Help - MangaDex", icon_url=bot.user.display_avatar
            )
            await ctx.respond(embed=embedVar)

        if category in ["MyAnimeList"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `mal`"
            embedVar.add_field(
                name="`seasons list`",
                value="Returns animes for the given season and year",
                inline=True,
            )
            embedVar.add_field(
                name="`seasons upcoming`",
                value="Returns anime for the upcoming season",
                inline=True,
            )
            embedVar.add_field(
                name="`random anime`", value="Fetches a random anime from MAL"
            )
            embedVar.add_field(
                name="`random manga`",
                value="Fetches a random manga from MAL",
                inline=True,
            )
            embedVar.add_field(
                name="`search anime`",
                value="Fetches up to 5 anime from MAL",
                inline=True,
            )
            embedVar.add_field(
                name="`search manga`",
                value="Fetches up to 5 manga from MAL",
                inline=True,
            )
            embedVar.add_field(
                name="`user`",
                value="Fetches the user's profile from MAL",
                inline=True,
            )
            embedVar.set_author(
                name="Help - MyAnimeList", icon_url=bot.user.display_avatar
            )
            await ctx.respond(embed=embedVar)

        if category in ["Tenor"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `tenor`"
            embedVar.add_field(
                name="`search multiple`",
                value="Searches for a single gif on Tenor",
                inline=True,
            )
            embedVar.add_field(
                name="`search one`",
                value="Searches for a single gif on Tenor",
                inline=True,
            )
            embedVar.add_field(
                name="`search suggestions`",
                value="Gives a list of suggested search terms based on the given topic",
                inline=True,
            )
            embedVar.add_field(
                name="`featured`",
                value="Returns up to 25 featured gifs from Tenor",
                inline=True,
            )
            embedVar.add_field(
                name="`trending terms`",
                value="Returns a list of trending search terms",
                inline=True,
            )
            embedVar.add_field(
                name="`random`",
                value="Gives out 25 random gifs from Tenor based on the given search term",
                inline=True,
            )
            embedVar.set_author(name="Help - Tenor", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)

        if category in ["Utility"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.add_field(
                name="`ffmpegcve`",
                value="Apparently convert video files to mp4",
                inline=True,
            )
            embedVar.add_field(
                name="`ping`",
                value="The Lag-o-meter, often lies",
                inline=True,
            )
            embedVar.add_field(
                name="`hypixel-count`",
                value="Returns the amount of players in each game server",
                inline=True,
            )
            embedVar.add_field(
                name="`version`",
                value="Returns the current version of Reina",
                inline=True,
            )
            embedVar.add_field(
                name="`uptime`",
                value="Returns the uptime for Reina",
                inline=True,
            )
            embedVar.set_author(name="Help - Utility", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)

        if category in ["Waifu"]:
            bot = self.bot
            embedVar = discord.Embed(color=discord.Color.from_rgb(255, 196, 253))
            embedVar.description = "Base command: `waifu`"
            embedVar.add_field(
                name="`random one`",
                value="Gets one random waifu pics",
                inline=True,
            )
            embedVar.add_field(
                name="`random many`",
                value="Returns many random waifu pics",
                inline=True,
            )
            embedVar.add_field(
                name="`pics`",
                value="Returns a random image of a waifu from waifu.pics",
                inline=True,
            )
            embedVar.set_author(name="Help - Waifu", icon_url=bot.user.display_avatar)
            await ctx.respond(embed=embedVar)


def setup(bot):
    bot.add_cog(ReinaHelp(bot))
