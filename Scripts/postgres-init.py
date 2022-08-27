import asyncio
import os
import sys
from pathlib import Path

import uvloop
from beryl_events_utils import BerylEventsUtils
from disquest_utils import DisQuestUsers
from dotenv import load_dotenv

path = Path(__file__).parents[1]
packagePath = os.path.join(path, "Bot", "genshin_wish_sim_utils")
envPath = os.path.join(path, "Bot", ".env")
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Bot"))

load_dotenv(envPath)

from genshin_wish_sim_utils import ReinaWSUtils
from help_utils import ReinaHelpUtils

POSTGRES_PASSWORD = os.getenv("Postgres_Password")
POSTGRES_SERVER_IP = os.getenv("Postgres_IP")
POSTGRES_EVENTS_DATABASE = os.getenv("Postgres_Events_Database")
POSTGRES_WS_DATABASE = os.getenv("Postgres_Wish_Sim_Database")
POSTGRES_DISQUEST_DATABASE = os.getenv("Postgres_Database")
POSTGRES_HELP_DATABASE = os.getenv("Postgres_Help_Database")
POSTGRES_USERNAME = os.getenv("Postgres_User")
POSTGRES_PORT = os.getenv("Postgres_Port")
EVENTS_CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_EVENTS_DATABASE}"
DISQUEST_CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DISQUEST_DATABASE}"
WS_CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_WS_DATABASE}"
HELP_CONNECTION_URI = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_HELP_DATABASE}"

utils = DisQuestUsers()
eventUtils = BerylEventsUtils()
wsUtils = ReinaWSUtils()
helpUtils = ReinaHelpUtils()


async def main():
    await utils.initTables(uri=DISQUEST_CONNECTION_URI)
    await eventUtils.initTables(uri=EVENTS_CONNECTION_URI)
    await wsUtils.initAllWSTables(uri=WS_CONNECTION_URI)
    await helpUtils.initAllHelpTables(uri=HELP_CONNECTION_URI)


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(main())
