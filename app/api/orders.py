from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import order as schemas
from app.crud import orders as crud
from app.core.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.OrderOut)
def create_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order_data)


@router.get("/", response_model=list[schemas.OrderOut])
def get_orders(email: str, db: Session = Depends(get_db)):
    return crud.get_orders_by_email(db, email)
