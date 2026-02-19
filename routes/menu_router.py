from fastapi import APIRouter, HTTPException, status
from api_schemas.menu_schema import MenuItemRead
from database import DB_dependency
from db_models.menu_model import Menu_DB


menu_router = APIRouter()


@menu_router.get("/", response_model=list[MenuItemRead])
def get_all_menu_items(db: DB_dependency):
    menu_item = db.query(Menu_DB).all()
    return menu_item
