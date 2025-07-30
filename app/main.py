import os
import logging
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.api import furniture, orders
from app.core.database import Base, engine
from app.models import furniture as furniture_model
from app.models import order as order_model

os.makedirs("logs", exist_ok=True)

app_logger = logging.getLogger("app.access")
app_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/access.log")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

app_logger.addHandler(file_handler)

Base.metadata.create_all(bind=engine)

app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        app_logger.info(f"{request.method} {request.url.path} - {response.status_code}")
        return response


app.add_middleware(LoggingMiddleware)

app.include_router(furniture.router, prefix="/furniture", tags=["Furniture"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
