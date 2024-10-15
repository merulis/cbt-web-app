from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_driver: str = "postgresql+asyncpg"
    db_user: str = "postgres"
    db_pass: str = "postgres"
    db_address_server: str = "localhost"
    db_name: str = "dev_db"
    db_url: str = f"{db_driver}://{db_user}:{db_pass}@{db_address_server}/{db_name}"
    db_echo: bool = True  # only for dev


settings = Settings()
