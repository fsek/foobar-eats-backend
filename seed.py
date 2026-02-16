from fastapi import FastAPI
from requests import session
from sqlalchemy.orm import Session
from db_models.example_model import Fruit_DB
from db_models.menu_model import menu_item


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


def seed_menu(db: Session):
    menu = [
        menu_item(
            name="Bröd",
            price=10,
            description="Stenugnsbakat surdegsbröd",
            ingredients=["Vetemjöl", "Jäst", "Rågmjöl", "Salt"],
        ),
        menu_item(
            name="Kaffe",
            price=6,
            description="Mörkrost",
            ingredients=["Kaffe", "Vatten"],
        ),
        menu_item(
            name="Citronkladdkaka",
            price=10,
            description="Syrlig och god",
            ingredients=["Smör", "Ägg", "Vetemjöl", "Citron", "Socker", "Vaniljsocker"],
        ),
    ]

    for item in menu:
        db.add(item)

    db.commit()
    return menu


"""
def seed_if_empty(app: FastAPI, db: Session):
    # If there are fruits, assume DB is already seeded
    if db.query(Fruit_DB).count() > 0:
        return

    print("Time to seed.")
    seed_fruits(db)
    print("Done seeding!")
"""


# """
def seed_if_empty(app: FastAPI, db: Session):
    # If there are fruits, assume DB is already seeded
    if db.query(menu_item).count() > 0:
        return

    print("Time to seed.")
    seed_menu(db)
    print("Done seeding!")


# """
