from sqlalchemy import Column, String, Integer
from models import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    measurement_unit = Column(String(200))
