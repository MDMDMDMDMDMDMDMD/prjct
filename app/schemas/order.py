from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime
from app.schemas.furniture import FurnitureOut


class OrderCreate(BaseModel):
    email: EmailStr
    furniture_ids: List[int]


class OrderOut(BaseModel):
    id: int
    email: EmailStr
    total: float
    created_at: datetime
    furniture: List[FurnitureOut]

    class Config:
        from_attributes = True
