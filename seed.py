from fastapi import FastAPI
from sqlalchemy.orm import Session
from db_models.example_model import Fruit_DB


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


def seed_if_empty(app: FastAPI, db: Session):
    # If there are fruits, assume DB is already seeded
    if db.query(Fruit_DB).count() > 0:
        return

    print("Time to seed.")
    seed_fruits(db)
    print("Done seeding!")
