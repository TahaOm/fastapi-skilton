import logging
import traceback
from typing import AsyncGenerator
from contextlib import asynccontextmanager
import sentry_sdk
from fastapi import FastAPI, HTTPException


from app.core.config import settings, log_settings

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    log_settings(settings)
    yield
    # Shutdown
    logging.getLogger("uvicorn").info("Shutting down app...")


# @asynccontextmanager
# async def lifespan(_application: FastAPI) -> AsyncGenerator:
#     # Startup
#     pool = aioredis.ConnectionPool.from_url(
#         str(settings.REDIS_URL), max_connections=10, decode_responses=True
#     )
#     redis.redis_client = aioredis.Redis(connection_pool=pool)

#     yield

#     if settings.ENVIRONMENT.is_testing:
#         return
#     # Shutdown
#     await pool.disconnect()


app = FastAPI(
    # **app_configs,
    lifespan=lifespan
)

# if settings.ENVIRONMENT.is_deployed:
#     sentry_sdk.init(
#         dsn=settings.SENTRY_DSN,
#         environment=settings.ENVIRONMENT,
#     )

# if settings.ENVIRONMENT != "local":
#     sentry_sdk.init(
#         dsn=settings.SENTRY_DSN,
#         enable_tracing=True,
#         profiles_sample_rate=1.0,
#         traces_sample_rate=1.0,
#     )


@app.get("/error")
def cause_error():
    try:
        1 / 0
    except ZeroDivisionError:
        logging.getLogger("uvicorn").error(
            "ZeroDivisionError occurred in /error endpoint"
        )
        logging.getLogger("uvicorn").error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Zero Division Error occurred")

    """with sentry"""
    # try:
    #     raise ValueError("An error occurred")
    # except Exception as e:
    #     logging.error(f"An error occurred: {e}")
    #     sentry_sdk.capture_exception(e)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
