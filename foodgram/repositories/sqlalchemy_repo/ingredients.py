from typing import List
from sqlalchemy import and_

from sqlalchemy.future import select

from repositories import BaseRepository
from models.ingredients import Ingredient, CreateIngredient, FilterIngredients
from repositories.sqlalchemy_repo.schemas import IngredientTable
from repositories.sqlalchemy_repo.db import Database
from repositories.sqlalchemy_repo.handle_response import handle_response


database = Database()


class IngredientRepository(BaseRepository):
    @handle_response(output_model=Ingredient)
    async def create(self, cmd: CreateIngredient) -> Ingredient:
        async with database.async_session() as session:
            ingredient = IngredientTable(
                name=cmd.name,
                measurement_unit=cmd.measurement_unit
            )
            session.add(ingredient)
            await session.commit()
            return ingredient

    @handle_response(output_model=Ingredient)
    async def read(self, pk: int) -> Ingredient:
        async with database.async_session() as session:
            ingredient = await session.execute(
                select(IngredientTable).filter(IngredientTable.pk == pk)
            )
            return ingredient.scalar()

    def __make_filters__(self, filter: FilterIngredients) -> List:
        filters = []
        if filter.name:
            filters.append(IngredientTable.name.ilike(f'{filter.name}%'))
        return filters

    @handle_response(output_model=Ingredient)
    async def read_all(self, filters: FilterIngredients) -> List[Ingredient]:
        async with database.async_session() as session:
            ingredients = await session.execute(
                select(IngredientTable).filter(
                    and_(*self.__make_filters__(filters))
                )
            )
            return ingredients.scalars().all()
