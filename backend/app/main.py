import logging

from contextlib import asynccontextmanager
from tenacity import (
    after_log,
    before_log,
    retry,
    stop_after_attempt,
    wait_fixed,
)

from fastapi import FastAPI

from app.api.router import api_router
from app.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # pre start actions
    yield
    # pre shutdown actions


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=settings.LOG.LOG_PATH / "log_backend.log",
    format=settings.LOG.FORMAT,
    level=logging.INFO,
)

app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
)

app.include_router(api_router)


@retry(
    stop=stop_after_attempt(settings.LOG.RETRY_MAX_TRIES),
    wait=wait_fixed(settings.LOG.RETRY_WAIT_SEC),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def main():
    import uvicorn

    logger.info("Uvicorn run app")
    uvicorn.run(app="main:app", reload=True)
    logger.info("Uvicorn shutdown app")


if __name__ == "__main__":
    main()
