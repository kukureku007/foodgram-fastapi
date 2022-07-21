from typing import Optional
from pydantic import BaseModel, constr


class BaseAPIModel(BaseModel):
    class Config:
        orm_mode = True


class Tag(BaseAPIModel):
    pk: int
    name: str
    color: str
    slug: str


class CreateTag(BaseAPIModel):
    name: str
    color: str
    # https://github.com/samuelcolvin/pydantic/issues/2872
    # F722 on regex
    # check slug pattern from Django
    slug: constr(regex=r'^[-a-zA-Z0-9_]+\Z')


class Ingredient(BaseAPIModel):
    pk: int
    name: str
    measurement_unit: str


class FilterIngredients(BaseAPIModel):
    name: Optional[str]


class CreateIngredient(BaseAPIModel):
    name: str
    measurement_unit: str
