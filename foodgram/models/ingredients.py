from typing import Optional

from models import BaseAPIModel


class Ingredient(BaseAPIModel):
    pk: int
    name: str
    measurement_unit: str


class FilterIngredients(BaseAPIModel):
    name: Optional[str]


class CreateIngredient(BaseAPIModel):
    name: str
    measurement_unit: str
