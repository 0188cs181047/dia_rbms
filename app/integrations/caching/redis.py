import json
from typing import Any, Optional

from redis.asyncio import Redis

from app.core.config import settings
from app.integrations.caching.base import CacheBackend


class RedisCache(CacheBackend):
    def __init__(self):
        self.client: Redis | None = None

    async def connect(self) -> None:
        self.client = Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True,
        )

        await self.client.ping()

    async def disconnect(self) -> None:
        if self.client:
            await self.client.aclose()

    async def ping(self) -> bool:
        return await self.client.ping()

    async def get(self, key: str) -> Optional[Any]:
        value = await self.client.get(key)

        if value is None:
            return None

        try:
            return json.loads(value)
        except Exception:
            return value

    async def set(
        self,
        key: str,
        value: Any,
        expire: int | None = None,
    ) -> bool:
        if isinstance(value, (dict, list)):
            value = json.dumps(value)

        return await self.client.set(
            key,
            value,
            ex=expire,
        )

    async def delete(self, key: str) -> bool:
        return bool(await self.client.delete(key))

    async def exists(self, key: str) -> bool:
        return bool(await self.client.exists(key))

    async def clear(self) -> bool:
        return await self.client.flushdb()