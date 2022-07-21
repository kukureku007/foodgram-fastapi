from typing import List

from pydantic import Field
from fastapi import APIRouter
# from fastapi import Depends

from models.tags import Tag, CreateTag
from services import TagService

# __all__ = ['tags_router']

tags_router = APIRouter(
    prefix='/api/tags',
)

tag_service = TagService()


@tags_router.get(
    '/',
    response_model=List[Tag]
)
async def get_all_tags():
    return await tag_service.read_all()


@tags_router.get(
    '/{pk}/',
    response_model=Tag
)
async def get_tag(
    pk: int = Field(..., title="Tag id(pk)", gt=0)
):
    return await tag_service.read(pk)


@tags_router.post(
    '/',
    response_model=Tag
)
async def create_tag(
    cmd: CreateTag
):
    return await tag_service.create(cmd)
