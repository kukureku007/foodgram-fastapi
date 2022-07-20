import asyncio

from repositories.sqlalchemy_repo.schemas import IngredientTable
# from sqlalchemy import delete, update, insert
from sqlalchemy.future import select
from repositories.sqlalchemy_repo.db import Database

database = Database()


async def add_ingredient_coro(name: str, measurement_unit: str):
    async with database.async_session() as session:
        obj = IngredientTable(
            name=name,
            measurement_unit=measurement_unit
        )
        session.add(obj)
        await session.commit()
        print(obj.name, obj.measurement_unit)

        res = await session.execute(
            select(IngredientTable)
        )
        for item in res.scalars().all():
            print(item.name, item.measurement_unit)


loop = asyncio.get_event_loop()


task = loop.create_task(add_ingredient_coro('строка1', 'строка1mu'))

loop.run_until_complete(task)

print('end')
