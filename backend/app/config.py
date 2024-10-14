from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_driver: str = "postgresql+asyncpg"
    db_user: str = "postgres"
    db_pass = ""
    db_address_server: str = "localhost"
    db_name: str = "db_name"
    db_url: str = f"{DB_DRIVER}://{DB_USER}:{DB_PASSSWORD}@{DB_SERVER}/{DB_NAME}"
