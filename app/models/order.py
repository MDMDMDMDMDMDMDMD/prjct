from sqlalchemy import Column, Integer, String, Float, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

order_furniture = Table(
    "order_furniture",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("furniture_id", Integer, ForeignKey("furniture.id"))
)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    furniture = relationship("Furniture", secondary=order_furniture)
