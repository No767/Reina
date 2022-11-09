import logging
import os
import sys
from pathlib import Path

import discord
from dotenv import load_dotenv
from reina_core import ReinaCore

# Set up needed intents
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

path = Path(__file__).parents[1]
packagePath = os.path.join(str(path), "Bot", "Libs")
sys.path.append(packagePath)

REINA_TOKEN = os.getenv("Reina_Dev_Token")

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)
logging.getLogger("gql").setLevel(logging.WARNING)
logging.getLogger("tortoise").setLevel(logging.WARNING)

bot = ReinaCore(intents=intents)

bot.run(REINA_TOKEN)
