from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_DRIVER = "postgresql+asyncpg"
DB_USER = "postgres"
DB_PASSSWORD = ""
DB_SERVER = "localhost"
DB_NAME = "db_name"
DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSSWORD}@{DB_SERVER}/{DB_NAME}"


engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()
