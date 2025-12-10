from functools import lru_cache

from src.backend.core.settings.app import AppSettings


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()
