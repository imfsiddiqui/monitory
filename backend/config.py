from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn, RedisDsn
from typing import Literal

class Settings(BaseSettings):
    # App Config
    app_name: str = Field("FastAPI App", env="APP_NAME")
    debug: bool = Field(False, env="DEBUG")
    environment: Literal["dev", "staging", "prod"] = Field("dev", env="ENVIRONMENT")

    # Server Config
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")

    # Security
    secret_key: str = Field(..., env="SECRET_KEY")  # ... means required
    algorithm: str = Field("HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Database
    database_url: PostgresDsn = Field(..., env="DATABASE_URL")
    redis_url: RedisDsn | None = Field(None, env="REDIS_URL")

    # CORS
    cors_origins: list[str] = Field(["*"], env="CORS_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignore extra env variables

settings = Settings()
