import asyncio
import logging

import uvloop
from discord.utils import utcnow
from rin_exceptions import NoItemsError

from .context_manager import ReinaEventsContextManager
from .models import ReinaEvents

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)


async def ReinaEventsChecker(uri: str, models: list):
    """A coroutine that manages and checks off any unactive events as needed

    Args:
        uri (str): DB Connection URI
        models (list): Models to be used
    """
    async with ReinaEventsContextManager(uri=uri, models=models):
        getUpcomingEvents = await ReinaEvents.filter(event_passed=False).all().values()
        currTime = utcnow()
        try:
            if len(getUpcomingEvents) == 0:
                raise NoItemsError
            else:
                for items in getUpcomingEvents:
                    eventDate = items["event_date"]
                    if eventDate <= currTime:
                        await ReinaEvents.filter(
                            event_item_uuid=items["event_item_uuid"]
                        ).update(event_passed=True)
        except NoItemsError:
            logging.warn(
                "No events either cannot be found, or have all passed. Will continue to check for more"
            )


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
