from fastapi import APIRouter, HTTPException, status
from api_schemas.menu_schema import MenuRead
from database import DB_dependency
from db_models.menu_model import menu_item

menu_router = APIRouter() 

@menu_router.get("/", response_model=list[MenuRead])
def get_all_items(db: DB_dependency):
    fruit = db.query(menu_item).all()
    return fruit

@menu_router.get("/{fruit_id}", response_model=MenuRead)
def get_item(fruit_id: int, db: DB_dependency):
    fruit = db.query(menu_item).filter_by(id=fruit_id).one_or_none()
    if fruit is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return fruit
"""
@menu_router.post("/", response_model=MenuRead)
def create_fruit(fruit_data: FruitCreate, db: DB_dependency):
    fruit = Fruit_DB(
        name=fruit_data.name,
        color=fruit_data.color,
        price=fruit_data.price,
    )
    db.add(fruit)
    db.commit()
    return fruit
"""