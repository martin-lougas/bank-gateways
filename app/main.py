import uuid

from fastapi import FastAPI, Request
from app.routes.account_statement_routes import router
from app.routes.authorization_routes import router as auth_router
import logging
import time

from logging.config import fileConfig

logging.config.fileConfig('app/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="Baltic Gateway service",
              version="0.0.1")

app.include_router(router)
app.include_router(auth_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    logger.info(f"request_id={request_id} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"request_id={request_id} completed_in={formatted_process_time}ms status_code={response.status_code}")

    return response
