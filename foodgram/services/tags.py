from typing import List
from models.tags import Tag, CreateTag

# from repositories import BaseRepository
from repositories.sqlalchemy_repo.tags import TagRepository

tag_repository = TagRepository()


class TagService:

    async def create(self, cmd: CreateTag) -> Tag:
        return await tag_repository.create(cmd)

    async def read(self, pk: int) -> Tag:
        return await tag_repository.read(pk)

    async def read_all(self) -> List[Tag]:
        return await tag_repository.read_all()
