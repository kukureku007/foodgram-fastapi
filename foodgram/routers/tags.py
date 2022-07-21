from fastapi import APIRouter
# from fastapi import Depends

from typing import List
from models.tags import Tag, CreateTag
from repositories.sqlalchemy_repo import TagRepository
from pydantic import Field
# __all__ = ['tags_router']

tags_router = APIRouter(
    prefix='/api/tags',
)

tag_repository = TagRepository()


@tags_router.get(
    '/',
    response_model=List[Tag]
)
async def get_all_tags():
    return await tag_repository.read_all()


@tags_router.get(
    '/{pk}/',
    response_model=Tag
)
async def get_tag(
    pk: int = Field(..., title="Tag id(pk)", gt=0)
):
    return await tag_repository.read(pk)


@tags_router.post(
    '/',
    response_model=Tag
)
async def create_tag(
    cmd: CreateTag
):
    return await tag_repository.create(cmd)
