from app.integrations.caching.cache_manager import get_cache, get_cache_type


class HealthService:

    @staticmethod
    async def cache_health():
        try:
            cache = get_cache()
            cache_type = get_cache_type()

            is_alive = await cache.ping()

            return {
                "status": "connected" if is_alive else "disconnected",
                "cache_type": cache_type,
            }

        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
            }