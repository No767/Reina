import asyncio

import numpy as np
import uvloop
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from . import models
from .models import Base


class ReinaHelpUtils:
    def __init__(self):
        self.self = self

    async def initAllHelpTables(self, uri: str) -> None:
        """Generates the tables needed for the help system

        Args:
            uri (str): Connection URI
        """
        engine = create_async_engine(
            uri,
            echo=True,
        )
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def addToHelpDB(
        self,
        uuid: str,
        name: str,
        parent_name: str,
        description: str,
        module: str,
        uri: str,
    ) -> None:
        """Adds a command to the DB

        Args:
            uuid (str): Command UUID
            name (str): Command Full Name
            parent_name (str): Parent Name for Command
            description (str): Description of the command
            module (str): Module for command
            uri (str): Connection URI
        """
        engine = create_async_engine(uri)
        asyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        async with asyncSession() as session:
            async with session.begin():
                addItem = models.HelpData(
                    uuid=uuid,
                    name=name,
                    parent_name=parent_name,
                    description=description,
                    module=module,
                )
                session.add_all([addItem])
                await session.commit()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getCmdsFromModule(self, module: str, uri: str) -> np.array:
        """Gets all commands that come from a module

        Args:
            module (str): Module where the command comes from
            uri (str): Connection URI

        Returns:
            np.array: An numpy array of `models.HelpData` classes
        """
        engine = create_async_engine(uri)
        asyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        async with asyncSession() as session:
            async with session.begin():
                selectItem = select(models.HelpData).filter(
                    models.HelpData.module == module
                )
                res = await session.execute(selectItem)
                return np.array([row for row in res.scalars()])

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def getAllCommands(self, uri: str) -> np.array:
        """Gets literally every single command in the DB

        Args:
            uri (str): Connection URI

        Returns:
            np.array: An `np.array` full of `models.HelpData` objects
        """
        engine = create_async_engine(uri)
        asyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        async with asyncSession() as session:
            async with session.begin():
                selItem = (
                    select(models.HelpData)
                    .order_by(models.HelpData.name.asc())
                    .filter(models.HelpData.module != "discord.commands.core")
                )
                res = await session.execute(selItem)
                return np.array([row for row in res.scalars()])

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
