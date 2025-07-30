from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderOut
from app.crud import orders as crud
from app.core.database import SessionLocal
from app.core.email import send_order_email
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=OrderOut)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    order = crud.create_order(db, order_data)

    if order is None:
        raise HTTPException(status_code=400, detail="Invalid furniture IDs")

    item_lines = [f"{item.name} - ${item.price:.2f}" for item in order.furniture]
    summary = "\n".join(item_lines)
    summary += f"\n\nTotal: ${order.total:.2f}"

    send_order_email(order.email, summary)

    return order


@router.get("/", response_model=list[OrderOut])
def get_orders(email: str, db: Session = Depends(get_db)):
    return crud.get_orders_by_email(db, email)
