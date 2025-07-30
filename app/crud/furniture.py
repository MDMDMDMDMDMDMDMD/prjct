from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas import furniture as schemas


def create_furniture(db: Session, furniture: schemas.FurnitureCreate):
    db_furniture = models.furniture.Furniture(**furniture.dict())
    db.add(db_furniture)
    db.commit()
    db.refresh(db_furniture)
    return db_furniture


def get_all_furniture(db: Session):
    return db.query(models.furniture.Furniture).all()


def get_furniture_by_id(db: Session, furniture_id: int):
    return db.query(models.furniture.Furniture).filter(models.furniture.Furniture.id == furniture_id).first()


def get_furniture_by_category(db: Session, category: str):
    return db.query(models.furniture.Furniture).filter(
        models.furniture.Furniture.category.ilike(category)
    ).all()
