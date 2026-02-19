from fastapi import FastAPI
from sqlalchemy.orm import Session
from db_models.example_model import Fruit_DB
from db_models.menu_model import Menu_DB


def seed_fruits(db: Session):
    fruits = [
        Fruit_DB(
            name="Apple",
            color="Red",
            price=30,
            # We don't seed the moldy state, it's init=False
        ),
        Fruit_DB(
            name="Banana",
            color="Yellow",
            price=20,
        ),
        Fruit_DB(
            name="Orange",
            color="Orange",
            price=25,
        ),
        Fruit_DB(
            name="Grape",
            color="Purple",
            price=50,
        ),
    ]

    for fruit in fruits:
        db.add(fruit)

    db.commit()
    return fruits


def seed_menu_items(db: Session):
    menu_items = [
        Menu_DB(
            name="Kaffe",
            description="Kaffe",
            price=10,
        ),
        Menu_DB(
            name="Kladdkaka",
            description="God!",
            price=20,
        ),
        Menu_DB(
            name="Schnitzel",
            description="Med pommes",
            price=100,
        ),
    ]

    for menu_item in menu_items:
        db.add(menu_item)

    db.commit()
    return menu_items


def seed_if_empty(app: FastAPI, db: Session):
    # If there are fruits, assume DB is already seeded
    if db.query(Menu_DB).count() > 0:
        return

    print("Time to seed.")
    seed_menu_items(db)
    print("Done seeding!")
