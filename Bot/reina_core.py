import asyncio
import logging
import os
import sys
from pathlib import Path

import discord
from discord.ext import tasks
from reina_events import ReinaEventsChecker

path = Path(__file__).parents[1]
packagePath = os.path.join(str(path), "Bot", "Libs")
sys.path.append(packagePath)


class ReinaCore(discord.Bot):
    def __init__(self, uri: str, models: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uri = uri
        self.models = models
        self.load_cogs()

    def load_cogs(self):
        path = Path(__file__).parents[0]
        cogsList = os.listdir(os.path.join(path, "Cogs"))
        for items in cogsList:
            if items.endswith(".py"):
                self.load_extension(f"Cogs.{items[:-3]}", store=False)

    @tasks.loop(seconds=5)
    async def eventHandler(self):
        await ReinaEventsChecker(uri=self.uri, models=self.models)

    @eventHandler.before_loop
    async def beforeReady(self):
        await self.wait_until_ready()

    @eventHandler.after_loop
    async def afterReady(self):
        if self.eventHandler.failed():
            logging.error(
                f"{self.user.name}'s Event Checker failed. Attempting to restart"
            )
            self.eventHandler.restart()
        elif self.eventHandler.is_being_cancelled():
            logging.info(f"Stopping {self.user.name}'s Event Checker")
            self.eventHandler.stop()

    async def on_ready(self):
        self.eventHandler.add_exception_type(asyncio.exceptions.TimeoutError)
        self.eventHandler.start()
        logging.info(f"Successfully started {self.user.name}'s Event Checker")
        logging.info(f"{self.user.name} is fully ready!")
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="/help")
        )
