from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseBotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        validate_assignment=True,
        env_file=".env",
        extra="ignore",
    )


class BotSettings(BaseBotSettings):
    telegram_token: str
    developer_chat_id: str


@lru_cache
def get_bot_settings() -> BotSettings:
    return BotSettings()
