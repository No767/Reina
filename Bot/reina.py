import asyncio
import logging
import os
import sys
import urllib.parse
from pathlib import Path

import discord
import uvloop
from dotenv import load_dotenv
from reinacore import ReinaCore

# Set up needed intents
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

path = Path(__file__).parents[1]
packagePath = os.path.join(str(path), "Bot", "Libs")
sys.path.append(packagePath)

REINA_TOKEN = os.getenv("Reina_Dev_Token")
POSTGRES_PASSWORD = urllib.parse.quote_plus(os.getenv("Postgres_Password"))
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_DATABASE = os.getenv("Postgres_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
CONNECTION_URI = f"asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)
logging.getLogger("gql").setLevel(logging.WARNING)
logging.getLogger("tortoise").setLevel(logging.WARNING)

bot = ReinaCore(uri=CONNECTION_URI, models=["reina_events.models"], intents=intents)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    bot.run(REINA_TOKEN)
