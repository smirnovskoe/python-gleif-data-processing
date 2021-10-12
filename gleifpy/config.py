from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    BATCH_SIZE: int = 10000

    DATABASE_URI: str = 'postgresql+psycopg2://postgres:12345@localhost:5432/gleif'

    class Config:
        _env_file = '.env',
        _env_file_encoding = 'utf-8'


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
