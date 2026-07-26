from datetime import date
from pydantic import BaseModel


class InventoryItemCreate(BaseModel):
    product_id: int
    quantity: float
    unit: str
    location: str
    expiration_date: date | None = None
    notes: str | None = None


class InventoryItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: float
    unit: str
    location: str
    expiration_date: date | None
    notes: str | None

    model_config = {"from_attributes": True}
