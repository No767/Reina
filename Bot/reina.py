import logging
import os
import sys
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Set up needed intents
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

path = Path(__file__).parents[1]
packagePath = os.path.join(str(path), "Libs")
sys.path.append(packagePath)

REINA_TOKEN = os.getenv("Reina_Dev_Token")

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)
logging.getLogger("gql").setLevel(logging.WARNING)

client = commands.Bot(intents=intents)

# Loads all Cogs
path = Path(__file__).parents[0]
cogsList = os.listdir(os.path.join(path, "Cogs"))
for items in cogsList:
    if items.endswith(".py"):
        client.load_extension(f"Cogs.{items[:-3]}", store=False)


@client.event
async def on_ready():
    logging.info("Reina is ready!")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="/reina help"
        )
    )


client.run(REINA_TOKEN)
