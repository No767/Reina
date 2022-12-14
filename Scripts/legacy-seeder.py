import asyncio
import logging
import os
import sys
from pathlib import Path

import uvloop
from dotenv import load_dotenv

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

POSTGRES_PASSWORD = os.getenv("Postgres_Password")
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_DATABASE = os.getenv("Postgres_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

from beryl_events_utils import BerylEventsUtils
from disquest_utils import DisQuestUsers
from genshin_wish_sim_utils import ReinaWSUtils

disquestUtils = DisQuestUsers()
berylEvents = BerylEventsUtils()
gwsUtils = ReinaWSUtils()


async def main():
    await disquestUtils.initTables(uri=CONNECTION_URI)
    await berylEvents.initTables(uri=CONNECTION_URI)
    await gwsUtils.initAllWSTables(uri=CONNECTION_URI)
    logging.info("[DB Seeder] Successfully seeded all tables!")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
