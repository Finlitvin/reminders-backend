from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.backend.database.database import (
    init_database,
    connect_to_database,
    close_db_connection,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # do if startup
    await init_database()
    app.state.database_session = await connect_to_database()
    yield
    # do if shutdown
    await close_db_connection(async_session=app.state.database_session)
