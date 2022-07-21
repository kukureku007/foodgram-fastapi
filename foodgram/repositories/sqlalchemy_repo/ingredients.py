from typing import List
from sqlalchemy import and_

from sqlalchemy.future import select

from repositories import BaseRepository
from models import Ingredient, CreateIngredient, FilterIngredients
from repositories.sqlalchemy_repo.schemas import IngredientTable
from repositories.sqlalchemy_repo.db import Database


database = Database()


class IngredientRepository(BaseRepository):
    async def create(self, cmd: CreateIngredient) -> Ingredient:
        async with database.async_session() as session:
            ingredient = IngredientTable(
                name=cmd.name,
                measurement_unit=cmd.measurement_unit
            )
            session.add(ingredient)
            await session.commit()
            return ingredient

    async def create_all(self) -> None:
        raise NotImplementedError

    async def read(self, pk: int) -> Ingredient:
        async with database.async_session() as session:
            ingredient = await session.execute(
                select(IngredientTable).filter(IngredientTable.pk == pk)
            )
            return Ingredient.from_orm(ingredient.scalar())

    def __make_filters__(self, filter: FilterIngredients) -> List:
        filters = []
        if filter.name:
            filters.append(IngredientTable.name.ilike(f'{filter.name}%'))
        return filters

    async def read_all(self, filters: FilterIngredients) -> List[Ingredient]:
        async with database.async_session() as session:
            ingredients = await session.execute(
                select(IngredientTable).filter(
                    and_(*self.__make_filters__(filters))
                )
            )
            return [
                Ingredient.from_orm(
                    ingredient
                ) for ingredient in ingredients.scalars().all()
            ]
