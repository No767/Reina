import asyncio
import logging
import os
import sys
import urllib.parse
from pathlib import Path

import uvloop
from dotenv import load_dotenv
from tortoise import Tortoise

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)

path = Path(__file__).parents[0]
packagePath = os.path.join(str(path), "Bot")
libsPath = os.path.join(str(path), "Bot", "Libs")
envPath = os.path.join(str(path), "Bot", ".env")
sys.path.append(packagePath)
sys.path.append(libsPath)

load_dotenv(dotenv_path=envPath)

POSTGRES_PASSWORD = urllib.parse.quote_plus(os.getenv("Postgres_Password"))
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_DATABASE = os.getenv("Postgres_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
CONNECTION_URI = f"asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"


async def main():
    await Tortoise.init(
        db_url=CONNECTION_URI, modules={"models": ["reina_events.models"]}
    )
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
