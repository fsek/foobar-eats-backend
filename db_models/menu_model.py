from typing import Optional
from db_models.base_model import BaseModel_DB
from sqlalchemy.orm import mapped_column, Mapped

class menu_item(BaseModel_DB):
    __tablename__="Menu"

    id: Mapped[str] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    hasRunOut: Mapped[bool] = mapped_column(init=False, default=False)
    ingredients: Mapped[list[str]] = mapped_column()