from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_manager import db_manager


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with db_manager.session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise