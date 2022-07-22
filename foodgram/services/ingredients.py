from typing import List

from models.ingredients import Ingredient, CreateIngredient, FilterIngredients
from repositories.sqlalchemy_repo.ingredients import IngredientRepository


class IngredientService:

    _repository: IngredientRepository

    def __init__(self, ingredient_repository) -> None:
        self._repository = ingredient_repository

    async def create(self, cmd: CreateIngredient) -> Ingredient:
        return await self._repository.create(cmd)

    async def create_all(self, file_name: str) -> None:
        ...

    async def read(self, pk: int) -> Ingredient:
        return await self._repository.read(pk)

    async def read_all(self, filters: FilterIngredients) -> List[Ingredient]:
        return await self._repository.read_all(filters)
