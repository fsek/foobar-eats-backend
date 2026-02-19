from api_schemas.base_schema import BaseSchema


class MenuItemRead(BaseSchema):
    id: int
    name: str
    description: str
    price: int
