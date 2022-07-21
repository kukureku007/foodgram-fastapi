from fastapi import APIRouter, Query
# from fastapi import Depends

from typing import List
from models import Ingredient, FilterIngredients
from repositories.sqlalchemy_repo import IngredientRepository
from pydantic import Field


ingredient_router = APIRouter(
    prefix='/api/ingredients',
)

ingredient_repository = IngredientRepository()


@ingredient_router.get(
    '/{pk}/',
    response_model=Ingredient
)
async def read_ingredient(
    pk: int = Field(..., title="Ingredient id(pk)", gt=0),
):
    return await ingredient_repository.read(pk)


@ingredient_router.get(
    '/',
    response_model=List[Ingredient]
)
async def read_all_ingredient(
    name: str = Query(
        None,
        # min_length=2, max_length=5,
        description='search by name field'
    )
):
    return await ingredient_repository.read_all(
        FilterIngredients(name=name)
    )
