from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from .model.base import Base
from .settings.config import get_database_settings


settings = get_database_settings()
print(settings.database_url)
engine: AsyncEngine = create_async_engine(
    settings.database_url, echo=settings.echo, future=settings.future
)
LocalSession: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine,
    autoflush=settings.autoflush,
    autocommit=settings.autocommit,
    expire_on_commit=settings.expire_on_commit,
)

async def init_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def connect_to_database() -> AsyncSession:
    async_session = LocalSession()
    return async_session


async def close_db_connection(async_session: AsyncSession) -> None:
    await async_session.close()
    await engine.dispose()
