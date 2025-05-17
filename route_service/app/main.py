from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db import ensure_indexes
from app.routers import route_router
from app.routers.route_router import repo


@asynccontextmanager
async def lifespan(app: FastAPI):
    await repo.start()
    await ensure_indexes()
    yield
    await repo.stop()

app = FastAPI(
    title="Route Service",
    lifespan=lifespan,
)
app.include_router(route_router.router)


if __name__ == "__main__":
    uvicorn.run("main:main_app", host="0.0.0.0", port=8000, reload=True)
