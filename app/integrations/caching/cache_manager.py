# cache_manager.py

cache = None
cache_type = None


async def init_cache():
    global cache, cache_type

    from app.core.config import settings
    from app.integrations.caching.factory import CacheFactory

    cache_type = settings.CACHE_TYPE
    cache = await CacheFactory.get_cache()


def get_cache():
    if cache is None:
        raise RuntimeError("Cache not initialized")
    return cache


def get_cache_type():
    return cache_type