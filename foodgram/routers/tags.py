from typing import List

from pydantic import Field
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from dependency_container import AppContainer
from models.tags import Tag, CreateTag
from services.tags import TagService

# __all__ = ['tags_router']

tags_router = APIRouter(
    prefix='/api/tags',
)


@tags_router.get(
    '/',
    response_model=List[Tag]
)
@inject
async def get_all_tags(
    tag_service: TagService = Depends(Provide[AppContainer.tag_service])
):
    return await tag_service.read_all()


@tags_router.get(
    '/{pk}/',
    response_model=Tag
)
@inject
async def get_tag(
    pk: int = Field(..., title="Tag id(pk)", gt=0),
    tag_service: TagService = Depends(Provide[AppContainer.tag_service])
):
    return await tag_service.read(pk)


@tags_router.post(
    '/',
    response_model=Tag,
)
@inject
async def create_tag(
    cmd: CreateTag,
    tag_service: TagService = Depends(Provide[AppContainer.tag_service])
):
    return await tag_service.create(cmd)
