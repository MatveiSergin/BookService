from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from settings import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.ENGINE_ECHO,
    pool_size=settings.ENGINE_POOL_SIZE,
)
class ModelORM(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement='auto', primary_key=True)


db_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.drop_all)
        await conn.run_sync(ModelORM.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with db_session() as session:
        yield session