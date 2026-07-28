from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.inventory_item import InventoryItem
from app.schemas.inventory import (
    InventoryItemCreate,
    InventoryItemResponse,
)

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("/", response_model=list[InventoryItemResponse])
def get_inventory(
    db: Session = Depends(get_db),
):
    return db.query(InventoryItem).all()


@router.post("/", response_model=InventoryItemResponse)
def create_inventory_item(
    item: InventoryItemCreate,
    db: Session = Depends(get_db),
):
    db_item = InventoryItem(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
