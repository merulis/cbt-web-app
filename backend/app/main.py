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

from app.router import api_router
from app.config import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    # pre start actions
    yield
    # pre shutdown actions


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=config.LOG.LOG_PATH / "log_backend.log",
    format=config.LOG.FORMAT,
    level=logging.INFO,
)

app = FastAPI(
    lifespan=lifespan,
    title=config.PROJECT_NAME,
)

app.include_router(router=api_router, prefix=config.API_PREFIX)


@retry(
    stop=stop_after_attempt(config.LOG.RETRY_MAX_TRIES),
    wait=wait_fixed(config.LOG.RETRY_WAIT_SEC),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def main():
    import uvicorn

    logger.info("Uvicorn run app")
    uvicorn.run(app=config.RUN.APP, reload=True)
    logger.info("Uvicorn shutdown app")


if __name__ == "__main__":
    main()
