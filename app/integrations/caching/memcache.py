import json

import aiomcache

from app.integrations.caching.base import CacheBackend


class MemcachedCache(CacheBackend):
    def __init__(
        self,
        host: str,
        port: int,
    ):
        self.host = host
        self.port = port

        self.client = None

    async def connect(self) -> None:
        self.client = aiomcache.Client(
            self.host,
            self.port,
        )

    async def disconnect(self) -> None:
        if self.client:
            await self.client.close()

    async def ping(self) -> bool:
        try:
            await self.client.version()
            return True
        except Exception:
            return False

    async def get(self, key: str):
        data = await self.client.get(
            key.encode()
        )

        if not data:
            return None

        return json.loads(data.decode())

    async def set(
        self,
        key: str,
        value,
        expire: int | None = None,
    ) -> bool:
        await self.client.set(
            key.encode(),
            json.dumps(value).encode(),
            exptime=expire or 0,
        )

        return True

    async def delete(self, key: str) -> bool:
        await self.client.delete(
            key.encode()
        )
        return True

    async def exists(self, key: str) -> bool:
        data = await self.client.get(
            key.encode()
        )
        return data is not None

    async def clear(self) -> bool:
        await self.client.flush_all()
        return True