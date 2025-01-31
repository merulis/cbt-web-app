from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
)

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from app.config import config


class AsyncDataBase:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_session(self):
        """return new sqlalchemy.AsyncSession"""
        async with self.session_factory() as session:
            yield session
            await session.close()


class SyncDataBase:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_engine(url=url, echo=echo)
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_session(self):
        """return new sqlalchemy.Session"""
        with self.session_factory() as session:
            yield session


sync_db = SyncDataBase(
    str(config.DB.SQLITE_URL),
    config.DB.ECHO,
)

async_db = AsyncDataBase(
    str(config.DB.SQLALCHEMY_DATABASE_URL),
    config.DB.ECHO,
)
