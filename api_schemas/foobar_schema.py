from api_schemas.base_schema import BaseSchema
from enum import Enum


class OrderCreate(BaseSchema):
    items: list[int]  # The items to order.
    address: str  # The address to deliver the order to.
    note: str | None = ""  # Optional note for the order.


class MenuItemRead(BaseSchema):
    id: int  # Item ID, used when placing an order.
    name: str  # Name of the item
    description: str  # Description of the item.
    price: int  # Price of the item in whole SEK:.


class OrderRead(BaseSchema):
    id: int  # The ID of the order.
    items: list[int]  # The IDs of the items in the order.
    placed_at: str  # The time that the order was placed.
    status: str  # 1 - Pending, 2 - Processing, 3 - Completed.
    total: int  # The total cost of the order.
    address: str  # The address to deliver the order to.
    note: str


class OrderStatus(Enum):
    Pending = "Pending"
    Processing = "Proccesing"
    Completed = "Completed"
