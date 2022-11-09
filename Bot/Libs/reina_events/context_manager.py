import asyncio
from contextlib import asynccontextmanager

import uvloop
from tortoise import Tortoise


@asynccontextmanager
async def ReinaEventsContextManager(uri: str, models: list):
    """A context manager to simply the process of connecting to the database and any cleanup work with closing conenctions as needed

    Args:
        uri (str): DB Connection URI
        models (list): List of model
    """
    conn = await Tortoise.init(db_url=uri, modules={"models": models})
    try:
        yield conn
    finally:
        await Tortoise.close_connections()


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
