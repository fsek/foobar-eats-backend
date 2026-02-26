from typing import Optional
from db_models.base_model import BaseModel_DB
from sqlalchemy.orm import mapped_column, Mapped


class order_DB(BaseModel_DB):
    __tablename__ = "order_table"
    extend_existing = True

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    items: Mapped[list[int]] = mapped_column()

    placed_at: Mapped[int] = mapped_column()

    status: Mapped[str] = mapped_column()

    total: Mapped[int] = mapped_column()

    address: Mapped[str] = mapped_column()

    note: Mapped[str] = mapped_column()

    """
    id: int
    items: list[int]
    placed_at: str
    status: str
    total: int
    address: str
    note: str
    """
