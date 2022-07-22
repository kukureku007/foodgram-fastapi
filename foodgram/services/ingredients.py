from typing import List
from models.ingredients import Ingredient, CreateIngredient, FilterIngredients

# from repositories import BaseRepository
from repositories.sqlalchemy_repo.ingredients import IngredientRepository

ingredient_repository = IngredientRepository()


class IngredientService:

    def __init__(self) -> None:
        print('init ingr service')

    def __del__(self):
        print('del ingr service')

    async def create(self, cmd: CreateIngredient) -> Ingredient:
        return await ingredient_repository.create(cmd)

    async def create_all(self, file_name: str) -> None:
        ...

    async def read(self, pk: int) -> Ingredient:
        return await ingredient_repository.read(pk)

    async def read_all(self, filters: FilterIngredients) -> List[Ingredient]:
        return await ingredient_repository.read_all(filters)
