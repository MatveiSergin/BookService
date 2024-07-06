from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.v1.routers import router
from database.database import create_tables
from database.initial_data import init_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await init_data()
    yield

app = FastAPI(lifespan=lifespan,
              title="BookService")

app.include_router(router)