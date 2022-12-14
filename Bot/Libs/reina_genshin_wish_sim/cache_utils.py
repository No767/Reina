from typing import Dict, Union

from reina_cache import ReinaCache, commandKeyBuilder
from reina_utils import ReinaCM

from .models import WSUser, WSUserInv


class ReinaGWSCacheUtils:
    """Caching utils used in Reina's GWS"""

    def __init__(
        self, uri: str, models: list, redis_host: str, redis_port: int
    ) -> None:
        """Constructor for `ReinaGWSCacheUtils`

        Args:
            uri (str): Connection URI
            models (list): List of Tortoise ORM models
            redis_host (str): Redis Host
            redis_port (int): Redis Port
        """
        self.self = self
        self.uri = uri
        self.models = models
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.cache = ReinaCache(host=self.redis_host, port=self.redis_port)

    async def cacheUser(self, user_id: int, command_name: str) -> Union[Dict, None]:
        """Abstraction for caching user data

        The purpose of this is a helper coroutine that caches the guild data if not cached.
        If cached, it will return the cached data.

        Args:
            user_id (int): Discord User ID
            command_name (str): Command Name. Will be used to set up the key on Redis

        Returns:
            Union[Dict, None]: This will return the cached data if cached, else it will return the data from the DB.
            Or in the case the user is not found, it will return None.
        """
        key = commandKeyBuilder(
            prefix="cache",
            namespace="reina",
            id=user_id,
            command=f"{command_name}".replace(" ", "-"),
        )
        if await self.cache.cacheExists(key=key) is False:
            async with ReinaCM(uri=self.uri, models=self.models):
                userData = await WSUser.filter(user_id=user_id).first().values()
                if userData is None:
                    return None
                await self.cache.setDictCommandCache(key=key, value=userData, ttl=15)
                return userData
        else:
            return await self.cache.getDictCommandCache(key=key)

    async def cacheUserInv(
        self, user_id: int, command_name: str
    ) -> Union[Dict, str, None]:
        """Abstraction for caching the user inv for the GWS

        Args:
            user_id (int): Discord User ID
            command_name (str): Command Name. Will be used to set up the key on Redis

        Returns:
            Union[Dict, str, None]: This will return the cached data if cached, else it will return the data from the DB.
            Or in the case the user's inv is not found, it will return None.
        """
        key = commandKeyBuilder(
            prefix="cache",
            namespace="reina",
            id=user_id,
            command=f"{command_name}".replace(" ", "-"),
        )
        if await self.cache.cacheExists(key=key) is False:
            async with ReinaCM(uri=self.uri, models=self.models):
                userInvData = await WSUserInv.filter(user_id=user_id).values()
                if len(userInvData) == 0:
                    return None
                await self.cache.setBasicCommandCache(
                    key=key, value=userInvData, ttl=15
                )
                return userInvData
        else:
            return await self.cache.getBasicCommandCache(key=key)

    async def cacheUserInvItem(
        self, user_id: int, name: str, command_name: str
    ) -> Union[Dict, None]:
        """Abstraction for caching the user inv item

        Args:
            user_id (int): Discord User ID
            name (str): Item Name
            command_name (str): Command name. Will get used in the Redis key

        Returns:
            Union[Dict, None]: This will return the cached data if cached, else it will return the data from the DB.
            Or in the case the item in the user inv is not found, it will return None.
        """
        key = commandKeyBuilder(
            prefix="cache",
            namespace="reina",
            id=user_id,
            command=f"{command_name}".replace(" ", "-"),
        )
        if await self.cache.cacheExists(key=key) is False:
            async with ReinaCM(uri=self.uri, models=self.models):
                userInvItem = (
                    await WSUserInv.filter(user_id=user_id, name=name)
                    .get_or_none()
                    .values()
                )
                if userInvItem is None:
                    return None
                await self.cache.setDictCommandCache(key=key, value=userInvItem, ttl=30)
                return userInvItem
        else:
            return await self.cache.getDictCommandCache(key=key)
