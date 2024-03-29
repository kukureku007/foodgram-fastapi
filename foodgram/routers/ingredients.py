from typing import List

from fastapi import APIRouter, Query
from pydantic import Field
from fastapi import Depends

from models.ingredients import Ingredient, FilterIngredients
from services.ingredients import IngredientService
from dependency_container import AppContainer

from dependency_injector.wiring import inject, Provide


ingredient_router = APIRouter(
    prefix='/api/ingredients',
)


@ingredient_router.get(
    '/{pk}/',
    response_model=Ingredient
)
@inject
async def read_ingredient(
    pk: int = Field(..., title="Ingredient id(pk)", gt=0),
    ingredient_service: IngredientService = Depends(
        Provide[AppContainer.ingredient_service]
    )
):
    return await ingredient_service.read(pk)


@ingredient_router.get(
    '/',
    response_model=List[Ingredient]
)
@inject
async def read_all_ingredient(
    name: str = Query(
        None,
        # min_length=2, max_length=5,
        description='search by name field'
    ),
    ingredient_service: IngredientService = Depends(
        Provide[AppContainer.ingredient_service]
    )
):
    return await ingredient_service.read_all(
        FilterIngredients(name=name)
    )
