from api_schemas.foobar_schema import OrderStatus
from db_models.base_model import BaseModel_DB
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import JSON


class Order_DB(BaseModel_DB):
    __tablename__ = "order_table"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    items: Mapped[list[int]] = mapped_column(JSON)

    placed_at: Mapped[str] = mapped_column()

    status: Mapped[OrderStatus] = mapped_column()

    total: Mapped[int] = mapped_column()

    address: Mapped[str] = mapped_column()

    note: Mapped[str] = mapped_column(init=False, default="")


class Item_DB(BaseModel_DB):
    __tablename__ = "item_table"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    name: Mapped[str] = mapped_column()

    description: Mapped[str] = mapped_column()

    price: Mapped[int] = mapped_column()
