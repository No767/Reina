import logging
import os
from pathlib import Path

import discord


class ReinaCore(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_cogs()

    def load_cogs(self):
        path = Path(__file__).parents[0]
        cogsList = os.listdir(os.path.join(path, "Cogs"))
        for items in cogsList:
            if items.endswith(".py"):
                self.load_extension(f"Cogs.{items[:-3]}", store=False)

    async def on_ready(self):
        logging.info(f"{self.user.name} is fully ready!")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="/reina help"
            )
        )
