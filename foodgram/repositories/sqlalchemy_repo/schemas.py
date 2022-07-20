from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IngredientTable(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    measurement_unit = Column(String(200))

# class Tag

# class Author

# class Recipe

# 