from pydantic import BaseModel

class FurnitureBase(BaseModel):
    name: str
    price: float
    category: str

class FurnitureCreate(FurnitureBase):
    pass

class FurnitureOut(FurnitureBase):
    id: int

    class Config:
        orm_mode = True
