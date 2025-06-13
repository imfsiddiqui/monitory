from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from utils import load_dotenvs

load_dotenvs()

class AppConfig(BaseSettings):
    name: str = Field(..., alias="APP_NAME")
    debug: bool = Field(..., alias="DEBUG")
    environment: Literal["dev", "staging", "prod"] = Field(..., alias="ENVIRONMENT")

class ServerConfig(BaseSettings):
    host: str = Field(..., alias="HOST")
    port: int = Field(..., alias="PORT")

class SecurityConfig(BaseSettings):
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str | None = Field(None, alias="ALGORITHM")
    access_token_expire_minutes: int | None = Field(None, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

class DatabaseConfig(BaseSettings):
    url: PostgresDsn = Field(..., alias="POSTGRES_URL")

class CacheConfig(BaseSettings):
    url: RedisDsn | None = Field(None, alias="REDIS_URL")

class CORSConfig(BaseSettings):
    origins: list[str] = Field(..., alias="CORS_ORIGINS")

class Settings(BaseSettings):
    app: AppConfig = AppConfig()
    server: ServerConfig = ServerConfig()
    security: SecurityConfig = SecurityConfig()
    database: DatabaseConfig = DatabaseConfig()
    cache: CacheConfig = CacheConfig()
    cors: CORSConfig = CORSConfig()

settings = Settings()
