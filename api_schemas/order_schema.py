from numpy import place
from pydantic import BaseModel
from enum import Enum


from api_schemas.base_schema import BaseSchema


class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"


class OrderRead(BaseSchema):
    id: int
    items: list[int]
    placed_at: str
    status: OrderStatus
    total: int
    address: str
    note: str | None = None


class OrderCreate(BaseSchema):
    items: list[int]
    address: str
    note: str | None = None


class OrderUpdate(BaseSchema):
    items: list[int] | None = None
    address: str | None = None
    note: str | None = None
    status: str | None = None
