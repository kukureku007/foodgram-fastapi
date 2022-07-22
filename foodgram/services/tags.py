from typing import List

from models.tags import Tag, CreateTag
from repositories.sqlalchemy_repo.tags import TagRepository


class TagService:

    _repository: TagRepository

    def __init__(self, tag_repository: TagRepository) -> None:
        self._repository = tag_repository

    async def create(self, cmd: CreateTag) -> Tag:
        return await self._repository.create(cmd)

    async def read(self, pk: int) -> Tag:
        return await self._repository.read(pk)

    async def read_all(self) -> List[Tag]:
        return await self._repository.read_all()
