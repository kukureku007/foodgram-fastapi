from pydantic import BaseModel


class BaseAPIModel(BaseModel):
    class Config:
        orm_mode = True
