import os

from dotenv import load_dotenv
from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # Databases
    PG_URL: PostgresDsn = os.getenv("PG_URL")
    REDIS_URL: RedisDsn = os.getenv("REDIS_URL")

    # Hashing
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("HASH_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("EXPIRE_TOKEN")


settings = Settings()
