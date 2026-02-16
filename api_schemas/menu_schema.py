from api_schemas.base_schema import BaseSchema

class MenuRead(BaseSchema):
    id: str
    name: str
    price: int
    description: str
    hasRunOut: bool
    ingredients: list[str]
