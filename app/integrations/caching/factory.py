from app.integrations.caching.memcache import MemcachedCache
from app.integrations.caching.redis import RedisCache

from app.core.config import settings


class CacheFactory:

    @staticmethod
    async def get_cache():

        if settings.CACHE_TYPE == "redis":
            cache = RedisCache()

        elif settings.CACHE_TYPE == "memcached":
            cache = MemcachedCache()

        else:
            raise ValueError(
                f"Unsupported cache type: {settings.CACHE_TYPE}"
            )

        await cache.connect()

        return cache