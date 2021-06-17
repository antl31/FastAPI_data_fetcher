import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str = os.environ.get("DATABASE_URI")

    redis_host: str = os.environ.get("REDIS_HOST")
    redis_port: str = os.environ.get("REDIS_PORT")

    fake_api_url: str = os.environ.get("FAKE_API_URL")
    fake_api_secret_key: str = os.environ.get("FAKE_API_KEY")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
