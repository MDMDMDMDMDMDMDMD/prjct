from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.schemas import furniture as schemas
from app.crud import furniture as crud
from app.core.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.FurnitureOut])
def list_furniture(
    category: str | None = Query(default=None),  # Фильтрация по категории
    db: Session = Depends(get_db)
):
    if category:
        return crud.get_furniture_by_category(db, category)
    return crud.get_all_furniture(db)


@router.get("/{furniture_id}", response_model=schemas.FurnitureOut)
def get_furniture(furniture_id: int, db: Session = Depends(get_db)):
    item = crud.get_furniture_by_id(db, furniture_id)
    if not item:
        raise HTTPException(status_code=404, detail="Furniture not found")
    return item


@router.post("/", response_model=schemas.FurnitureOut, status_code=status.HTTP_201_CREATED)
def create_furniture(furniture: schemas.FurnitureCreate, db: Session = Depends(get_db)):
    return crud.create_furniture(db, furniture)
