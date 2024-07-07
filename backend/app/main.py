from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException, status
from api.v1.routers import router
from database.database import create_tables
from database.initial_data import init_data
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await init_data()
    yield

app = FastAPI(lifespan=lifespan,
              title="BookService")

app.include_router(router)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    auth_success = request.headers.get("x-auth-success")
    if auth_success == "False":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="authentication error")
    response = await call_next(request)
    return response

if __name__ == "__main__":
    uvicorn.run(app)