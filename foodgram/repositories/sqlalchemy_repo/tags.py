from typing import List, Callable
from contextlib import _AsyncGeneratorContextManager

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from repositories import BaseRepository
from models.tags import Tag, CreateTag
from repositories.sqlalchemy_repo.schemas import TagTable
from repositories.sqlalchemy_repo.handle_response import handle_response


class TagRepository(BaseRepository):
    async_session_factory: Callable[
        ..., _AsyncGeneratorContextManager[AsyncSession]
    ]

    def __init__(self, async_session_factory) -> None:
        self.async_session_factory = async_session_factory

    @handle_response(output_model=Tag)
    async def create(self, cmd: CreateTag) -> Tag:
        async with self.async_session_factory() as session:
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
        async with self.async_session_factory() as session:
            tag = await session.execute(
                select(TagTable).filter(TagTable.pk == pk)
            )
            return tag.scalar()

    @handle_response(output_model=Tag)
    async def read_all(self) -> List[Tag]:
        async with self.async_session_factory() as session:
            tags = await session.execute(
                select(TagTable)
            )
            return tags.scalars().all()
