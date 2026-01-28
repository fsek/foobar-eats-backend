from fastapi import APIRouter
from api_schemas.foobar_schema import *
from database import DB_dependency
from db_models.foobar_model import *


foobar_router = APIRouter()


@foobar_router.get("/", response_model=list[MenuItemRead])
def get_all_items(db: DB_dependency):
    item = db.query(Item_DB).all()
    return item
