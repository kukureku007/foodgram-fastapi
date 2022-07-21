from typing import List

from sqlalchemy.future import select

from repositories import BaseRepository
from models import Tag, CreateTag
from repositories.sqlalchemy_repo.schemas import TagTable
from repositories.sqlalchemy_repo.db import Database
from repositories.sqlalchemy_repo.handle_response import handle_response


database = Database()


class TagRepository(BaseRepository):

    @handle_response(output_model=Tag)
    async def create(self, cmd: CreateTag) -> Tag:
        async with database.async_session() as session:
            tag = TagTable(
                name=cmd.name,
                color=cmd.color,
                slug=cmd.slug
            )
            session.add(tag)
            await session.commit()
            return tag

    @handle_response(output_model=Tag)
    async def read(self, pk: int) -> Tag:
        async with database.async_session() as session:
            tag = await session.execute(
                select(TagTable).filter(TagTable.pk == pk)
            )
            return tag.scalar()

    @handle_response(output_model=Tag)
    async def read_all(self) -> List[Tag]:
        async with database.async_session() as session:
            tags = await session.execute(
                select(TagTable)
            )
            return tags.scalars().all()
