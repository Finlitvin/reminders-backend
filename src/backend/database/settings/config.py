from functools import lru_cache

from .base import BaseDatabaseSettings


class DatabaseSettings(BaseDatabaseSettings):
    db_driver: str = "postgresql+asyncpg"
    db_host: str
    db_name: str
    db_user: str
    db_password: str

    echo: bool = False
    future: bool = True
    autoflush: bool = False
    autocommit: bool = False
    expire_on_commit: bool = False

    @property
    def database_url(self) -> str:
        url = f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"

        return url


@lru_cache
def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings()
