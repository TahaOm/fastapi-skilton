import json
import secrets
from typing import Any
from pydantic import PostgresDsn, RedisDsn, field_validator, model_validator
from pydantic_settings import BaseSettings

from app.core.constants import Environment


class Settings(BaseSettings):
    # DATABASE_URL: PostgresDsn
    # REDIS_URL: RedisDsn

    SITE_DOMAIN: str

    ENVIRONMENT: Environment

    SENTRY_DSN: str

    # CORS_ORIGINS: List[str] = [os.getenv("CORS_ORIGINS")]
    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str
    CORS_HEADERS: list[str]

    APP_VERSION: str

    # JWT settings
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator("ENVIRONMENT")
    def parse_env(cls, v):
        # Auto-convert string to Enum, case-insensitive
        if isinstance(v, Environment):
            return v
        return Environment(v.upper())

    @field_validator("CORS_ORIGINS", "CORS_HEADERS", mode="before")
    def parse_json_lists(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON list format")
        return v

    @model_validator(mode="after")
    def validate_sentry_non_local(self) -> "Config":
        if self.ENVIRONMENT.is_deployed and not self.SENTRY_DSN:
            raise ValueError("Sentry is not set")

        return self


# Create an instance of the Settings class
settings = Settings()


def log_settings(settings):
    import logging
    from pprint import pformat

    logger = logging.getLogger("uvicorn")
    logger.info("Loaded settings:\n%s", pformat(settings.model_dump()))


app_configs: dict[str, Any] = {"title": "App API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
