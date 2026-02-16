from api_schemas.base_schema import BaseSchema


class MenuRead(BaseSchema):
    id: str
    name: str
    price: int
    description: str
    hasRunOut: bool
    ingredients: list[str]


class MenuCreate(BaseSchema):
    name: str
    color: str
    price: int | None = None


class MenuUpdate(BaseSchema):
    name: str | None = None
    color: str | None = None
    price: int | None = None
