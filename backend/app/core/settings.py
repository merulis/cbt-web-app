import secrets

from pathlib import Path

from pydantic import (
    PostgresDsn,
    computed_field,
    BaseModel,
)

from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


BACKEND_BASE_DIR = Path(__file__).parent.parent


class Logger(BaseModel):
    FORMAT: str = "%(levelname)s:%(asctime)s: %(name)s - %(message)s"
    LOG_PATH: Path = BACKEND_BASE_DIR.parent / "logs"
    RETRY_WAIT_SEC: int = 5
    RETRY_MAX_TRIES: int = RETRY_WAIT_SEC * 12


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


class AuthJWT(BaseModel):
    ACCESS_TYPE: str = "access"
    REFRESH_TYPE: str = "refresh"
    ALGORITHM: str = "RS256"
    PRIVATE_KEY: Path = BACKEND_BASE_DIR / "certs" / "jwt-private.pem"
    PUBLIC_KEY: Path = BACKEND_BASE_DIR / "certs" / "jwt-public.pem"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1  # 1 minutes only for dev
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


class Settings(BaseSettings):
    API_V1_STR: str = "api/v1"
    SECRETS_KEY: str = secrets.token_urlsafe(32)

    FRONEND_HOST: str = ""

    PROJECT_NAME: str = "CBT APP"

    LOG: Logger = Logger()

    DB: DBSettings = DBSettings()

    JWT: AuthJWT = AuthJWT()

    FIRST_SUPERUSER: str = ""
    FIRST_SUPERUSER_PASSWORD: str = ""


settings = Settings()
