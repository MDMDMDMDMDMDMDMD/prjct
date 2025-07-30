from sqlalchemy.orm import Session
from app import models, schemas


def create_order(db: Session, order_data: schemas.order.OrderCreate):
    items = db.query(models.furniture.Furniture).filter(models.furniture.Furniture.id.in_(order_data.furniture_ids)).all()
    total = sum(item.price for item in items)

    new_order = models.order.Order(
        email=order_data.email,
        furniture=items,
        total=total
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def get_orders_by_email(db: Session, email: str):
    return db.query(models.order.Order).filter(models.order.Order.email == email).all()
