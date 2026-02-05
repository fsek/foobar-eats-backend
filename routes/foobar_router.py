from datetime import datetime
from fastapi import APIRouter
from api_schemas.foobar_schema import *
from database import DB_dependency
from db_models.foobar_model import *
from fastapi import APIRouter, HTTPException, status


foobar_router = APIRouter()


@foobar_router.get("/menu", response_model=list[MenuItemRead])
def get_all_items(db: DB_dependency):
    item = db.query(Item_DB).all()
    return item


@foobar_router.post("/orders", response_model=OrderRead)
def create_order(order_data: OrderCreate, db: DB_dependency):
    items = order_data.items
    possible = db.query(Item_DB).all()

    if not all(map(lambda x: x in map(lambda y: y.id, possible), items)):
        # There is an item present that is not on the menu
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    total_price = 0
    for item in items:
        for menu_item in possible:
            if item == menu_item.id:
                total_price += menu_item.price
                break

    placed_time = datetime.now().strftime("%H:%M")

    order = Order_DB(
        items=order_data.items,
        total=total_price,
        address=order_data.address,
        status="Pending",
        placed_at=placed_time,
        note="" if order_data.note == None else order_data.note,
    )
    db.add(order)
    db.commit()
    return order
