from typing import Optional
from db_models.base_model import BaseModel_DB
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import JSON


class Order_DB(BaseModel_DB):
    __tablename__ = "order_table"
    extend_existing = True

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    # represents a list of item IDs; stored as JSON array in the database
    items: Mapped[list[int]] = mapped_column(JSON)

    placed_at: Mapped[str] = mapped_column(nullable=False)

    status: Mapped[str] = mapped_column(nullable=False)

    total: Mapped[int] = mapped_column(nullable=False)

    address: Mapped[str] = mapped_column(nullable=False)

    note: Mapped[str] = mapped_column(nullable=True)

    """
    id: int
    items: list[int]
    placed_at: str
    status: str
    total: int
    address: str
    note: str
    """
