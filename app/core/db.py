from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.PG_URL.unicode_string(), future=True, echo=True)
AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session
