from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # pre start actions
    yield
    # pre shutdown actions


app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", reload=True)
