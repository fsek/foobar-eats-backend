from numpy import place

from api_schemas.base_schema import BaseSchema

"""
class FruitRead(BaseSchema):
    id: int
    name: str
    color: str
    price: int
    is_moldy: bool


class FruitCreate(BaseSchema):
    name: str
    color: str
    price: int | None = None


class FruitUpdate(BaseSchema):
    name: str | None = None
    color: str | None = None
    price: int | None = None

"""


class OrderRead(BaseSchema):
    id: int
    items: list[int]
    placed_at: str
    status: str
    total: int
    address: str
    note: str


class OrderCreate(BaseSchema):
    items: list[int]
    address: str
    note: str


class OrderUpdate(BaseSchema):
    items: list[int] | None = None
    address: str | None = None
    note: str | None = None
    status: str | None = None
