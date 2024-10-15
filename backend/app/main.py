from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.db import database, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    # pre shutdown actions

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
