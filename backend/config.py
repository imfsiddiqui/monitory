from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, PostgresDsn, RedisDsn
from typing import Literal
import os

config = SettingsConfigDict(
    env_file = f".env.{os.getenv('ENVIRONMENT', 'dev')}",
    env_file_encoding = "utf-8",
    extra = "ignore", # Ignore extra env variables
)

class AppConfig(BaseSettings):
    model_config = config

    name: str = Field("FastAPI App", alias="APP_NAME")
    debug: bool = Field(False, alias="DEBUG")
    environment: Literal["dev", "staging", "prod"] = Field("dev", alias="ENVIRONMENT")

class ServerConfig(BaseSettings):
    model_config = config

    host: str = Field("0.0.0.0", alias="HOST")
    port: int = Field(8000, alias="PORT")

class SecurityConfig(BaseSettings):
    model_config = config

    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = Field("HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

class DatabaseConfig(BaseSettings):
    model_config = config

    url: PostgresDsn = Field(..., alias="DATABASE_URL")

class CacheConfig(BaseSettings):
    model_config = config

    url: RedisDsn | None = Field(None, alias="REDIS_URL")

class CORSConfig(BaseSettings):
    model_config = config

    origins: list[str] = Field(["*"], alias="CORS_ORIGINS")

class Settings(BaseSettings):
    app: AppConfig = AppConfig()
    server: ServerConfig = ServerConfig()
    security: SecurityConfig = SecurityConfig()
    database: DatabaseConfig = DatabaseConfig()
    cache: CacheConfig = CacheConfig()
    cors: CORSConfig = CORSConfig()

settings = Settings()
