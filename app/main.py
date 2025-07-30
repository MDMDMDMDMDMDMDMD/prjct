from fastapi import FastAPI
from app.api import furniture, orders
from app.core.database import Base, engine
from app.models import furniture as furniture_model
from app.models import order as order_model

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(furniture.router, prefix="/furniture", tags=["Furniture"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
