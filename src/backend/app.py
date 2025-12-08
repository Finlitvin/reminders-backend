from fastapi import FastAPI

from src.backend.core.config import get_app_settings
from src.backend.core.events import lifespan
from src.backend.api.v1.api import router as api_router


def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs, lifespan=lifespan)

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app: FastAPI = get_application()
