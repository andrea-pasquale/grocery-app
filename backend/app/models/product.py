from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    category: Mapped[str | None] = mapped_column(String(50), nullable=True)

    inventory_items: Mapped[list["InventoryItem"]] = relationship(
        back_populates="product"
    )
