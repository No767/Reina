import asyncio
import logging
import random
from hashlib import sha1

import uvloop
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands
from numpy.random import default_rng

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)


class fun_stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    fun = SlashCommandGroup("fun", "Some fun commands to use")
    funRandom = fun.create_subgroup("random", "Random commands")

    @fun.command(name="ship")
    async def shipPerson(
        self,
        ctx,
        person_a: Option(str, "The person who you would want to ship with"),
        person_b: Option(str, "The person you would want to ship with"),
    ):
        """Calculates how much love a person has"""
        a = person_a + person_b
        hashstr = sha1(bytes(a, "utf-8")).hexdigest()
        percentage = round(int(hashstr, 16) / 2**160 * 100, 2)
        if percentage < 20:
            lovePercentage = "smells like hatred!"
        elif percentage < 40:
            lovePercentage = "best stay apart!"
        elif percentage < 60:
            lovePercentage = "let's stay friends!"
        elif percentage < 85:
            lovePercentage = "the air buzzes with love!"
        else:
            lovePercentage = "true love is in the air!"
        await ctx.respond(f"Their love is {percentage}%. {lovePercentage}")

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @fun.command(name="sex")
    async def havingSex(
        self, ctx, person: Option(str, "The person who would want to be submissive")
    ):
        """it's a sex calculator"""
        sexsuccessresponses = [
            "You have successfully fucked {}! You were very submissive and breedable",
            "Ou la la! You successfully sexed {}! You were so breedable you bore their twins!",
        ]
        sexfailureresponses = [
            "You did not fuck {}. You were too dominant and unbreedable"
        ]
        if random.randint(0, 1):
            await ctx.respond(random.choice(sexsuccessresponses).format(person))
        else:
            await ctx.respond(random.choice(sexfailureresponses).format(person))

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @fun.command(name="say")
    async def sayTheWord(self, ctx, things: Option(str, "The word or phrase to say")):
        """Says something"""
        await ctx.respond(things.replace("@", ""))

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @fun.command(name="laugh")
    async def laughingAtSomeone(
        self, ctx, length: Option(int, "The length of the laugh")
    ):
        """Laughs"""
        laughter = "".join(
            [random.choice("ASDFGHJKL") for _ in range(min(length, 2001))]
        )
        await ctx.respond(laughter)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @funRandom.command(name="int")
    async def randint(
        self,
        ctx,
        floor: Option(int, "The base limit"),
        ceil: Option(int, "The upper limit"),
    ):
        """Based on 2 limits, returns a random number"""
        await ctx.respond(random.randint(int(floor), int(ceil)))

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @funRandom.command(name="dice")
    async def randomDice(
        self,
        ctx,
        *,
        num_of_sides: Option(int, "The number of sides that the dice has", default=6),
    ):
        """Randomly rolls the dice"""
        rng = default_rng()
        res = rng.integers(low=1, high=num_of_sides)
        await ctx.respond(f"It seems like you rolled a {res}!")

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def setup(bot):
    bot.add_cog(fun_stuff(bot))
