import secrets

from pydantic import (
    PostgresDsn,
    computed_field,
    BaseModel,
)

from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    POSTGRES_DRIVER: str = "postgresql+asyncpg"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "dev_db"
    ECHO: bool = False  # True only for dev

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme=self.POSTGRES_DRIVER,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


class Settings(BaseSettings):
    API_V1_STR: str = "api/v1"
    SECRETS_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    FRONEND_HOST: str = ""

    PROJECT_NAME: str = "CBT APP"

    DB: DBSettings = DBSettings()

    FIRST_SUPERUSER: str = ""
    FIRST_SUPERUSER_PASSWORD: str = ""


settings = Settings()
