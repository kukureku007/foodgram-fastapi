import asyncio
from datetime import datetime
# import datetime

from repositories.sqlalchemy_repo.schemas import IngredientTable, RecipeTable, TagTable
# from sqlalchemy import delete, update, insert
from sqlalchemy.future import select
from repositories.sqlalchemy_repo.db import Database


database = Database()


# from sqlalchemy_utils.functions import create_database, database_exists, drop_database
# if not database_exists(databse_url):
    # print('creating database')
    # create_database(databse_url)

# if __name__=='__main__':
    # if len(sys.argv) > 1 and sys.argv[1] == 'drop_database':
            # drop_database(databse_url)


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


async def add_tag_coro(name: str, color: str):
    async with database.async_session() as session:
        tag = TagTable(
            name=name,
            color=color
        )
        session.add(tag)
        await session.commit()

        res = await session.execute(
            select(TagTable)
        )
        for item in res.scalars().all():
            print(item.name, item.color)


async def add_recipe_coro1():
    async with database.async_session() as session:
        # print('in add recipe')
        res = await session.execute(
            # filter where - синонимы
            select(TagTable).filter(TagTable.pk.in_((1,2,3)))
            # select(TagTable).where(TagTable.pk == 1)
        )
        tags = res.scalars().all()
        for tag in tags:
            print(tag.name, tag.color, tag.pk)
        # print('recipe: ', tag, type(tag))
        recipe = RecipeTable(
            name='name2',
            cooking_time=12,
            text='some big text',
            pub_date=datetime.now(),
            image_path='/recipes/sdaadadad.png'
        )

        # добавить list
        recipe.tags.extend(tags[:-1])
        # добавить один
        recipe.tags.append(tags[-1])
        session.add(recipe)
        await session.commit()
        print(len(recipe.tags))
        # удаление
        recipe.tags.remove(tags[-1])
        await session.commit()
        print(len(recipe.tags))
        print('recipe_pk: ', recipe.pk)


loop = asyncio.get_event_loop()

# loop.create_task(add_tag_coro('завтрак', 'белый'))
# loop.create_task(add_ingredient_coro('сахар', 'г.'))
# loop.create_task(add_recipe_coro())

tasks = asyncio.all_tasks(loop=loop)

group = asyncio.gather(*tasks)
loop.run_until_complete(group)

print('end')

# Cascade on delete ???