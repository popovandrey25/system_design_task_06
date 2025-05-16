import uvicorn
from fastapi import FastAPI

from app.routers import trip_router

app = FastAPI(title="User Service")
app.include_router(trip_router.router)


if __name__ == "__main__":
    uvicorn.run("main:main_app", host="0.0.0.0", port=8000, reload=True)
