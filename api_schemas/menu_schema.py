from api_schemas.base_schema import BaseSchema


class MenuRead(BaseSchema):
    id: int
    name: str
    price: int
    description: str
    hasRunOut: bool
    ingredients: str


class MenuCreate(BaseSchema):
    name: str
    # color: str
    price: int | None = None
    description: str
    ingredients: str


class MenuUpdate(BaseSchema):
    name: str | None = None
    # color: str | None = None
    price: int | None = None
    description: str | None = None
    ingredients: str | None = None
