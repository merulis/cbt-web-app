from app.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DataBase:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocmmit=False,
            expire_on_commit=False,
        )


database = DataBase(settings.db_url, settings.db_echo)
