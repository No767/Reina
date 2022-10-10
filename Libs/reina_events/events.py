import asyncio
import uuid
from datetime import datetime

import uvloop
from tortoise import Tortoise
from tortoise.transactions import in_transaction

from . import ReinaEvents


class ReinaEventsUtils:
    def __init__(self, uri: str, models: list):
        self.self = self
        self.uri = uri
        self.models = models

    async def addEvent(
        self,
        uuid: uuid.uuid4(),
        user_id: int,
        name: str,
        description: str,
        date_added: datetime,
        event_date: datetime,
        event_passed: bool,
    ) -> None:
        """Adds an event into the DB

        Args:
            uuid (uuid.uuid4): The UUID4 of the event
            user_id (int): Discord user ID
            name (str): Event name
            description (str): Event description
            date_added (datetime): The date that the event was added
            event_date (datetime): The date of the event
            event_passed (bool): Whether the event has passed or not
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        async with in_transaction() as conn:
            await ReinaEvents.create(
                uuid=uuid,
                user_id=user_id,
                name=name,
                description=description,
                date_added=date_added,
                event_date=event_date,
                event_passed=event_passed,
                using_db=conn,
            )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getAllUserEvents(self, user_id: int) -> list:
        """Gets all of the events belonging to the user

        Args:
            user_id (int): Discord user ID

        Returns:
            list: A list of `dict` objects
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        return await ReinaEvents.filter(user_id=user_id).values()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getAllUserEventsName(self, user_id: int, name: str) -> list:
        """Gets the event via the name

        Args:
            user_id (int): Discord user ID
            name (str): Event name

        Returns:
            list: A list of `dict` objects
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        return await ReinaEvents.filter(user_id=user_id, name=name).values()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getFirstUserEventsName(self, user_id: int, name: str) -> dict:
        """Gets the event via the name

        Args:
            user_id (int): Discord user ID
            name (str): Event name

        Returns:
            dict: A `dict` object or `None`
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        return await ReinaEvents.filter(user_id=user_id, name=name).first().values()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getUserEventPassedStatus(self, user_id: int, event_passed: bool) -> list:
        """Gets any passed or not passed events belonging to that user

        Args:
            user_id (int): Discord user ID
            event_passed (bool): Whether the event has passed or not

        Returns:
            list: A list of `dict` objects
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        return await ReinaEvents.filter(
            user_id=user_id, event_passed=event_passed
        ).values()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def setEventPassedStatus(
        self, user_id: int, uuid: str, event_passed: bool
    ) -> None:
        """Sets the status of the event

        Args:
            user_id (int): Discord user ID
            uuid (str): The UUID4 of the event
            event_passed (bool): Whether the event has passed or not
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        await ReinaEvents.filter(user_id=user_id, uuid=uuid).update(
            event_passed=event_passed
        )

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def purgeAllUserEvents(self, user_id: int) -> None:
        """Purges all of the user events data belonging to that user

        Args:
            user_id (int): Discord user ID
        """
        await Tortoise.init(db_url=self.uri, modules={"models": self.models})
        await ReinaEvents.filter(user_id=user_id).delete()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
