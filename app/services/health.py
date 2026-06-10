from app.integrations.caching.cache_manager import get_cache, get_cache_type
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession



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
        
    @staticmethod
    async def check_health(db: AsyncSession):
        try:
            result = await db.execute(text("SELECT 1"))
            value = result.scalar()

            if value == 1:
                return {
                    "status": "connected",
                    "service": "postgres",
                }

            return {
                "status": "unhealthy",
                "service": "postgres",
            }

        except Exception as e:
            return {
                "status": "error",
                "service": "postgres",
                "error": str(e),
            }