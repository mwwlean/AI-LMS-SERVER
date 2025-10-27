from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = Field(default="AI LMS API", alias="APP_NAME")
    database_url: str = Field(..., alias="DATABASE_URL")
    openrouter_api_key: str = Field(default="", alias="OPENROUTER_API_KEY")
    openrouter_model: str = Field(..., alias="OPENROUTER_MODEL")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


