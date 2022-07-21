from pydantic import constr

from models import BaseAPIModel


class Tag(BaseAPIModel):
    pk: int
    name: str
    color: str
    slug: str


class CreateTag(BaseAPIModel):
    name: str
    color: str
    # https://github.com/samuelcolvin/pydantic/issues/2872
    # F722 on regex
    # check slug pattern from Django
    slug: constr(regex=r'^[-a-zA-Z0-9_]+\Z')
