from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_URL


# TODO add logging
class Database:
    engine: AsyncEngine

    def __init__(self):
        print('INIT engine')
        self.engine = create_async_engine(DATABASE_URL, future=True, echo=True)

    @asynccontextmanager
    async def async_session(self) -> AsyncGenerator[AsyncSession, None]:
        session_maker = sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )
        # closing session on aexit()
        async with session_maker() as session:
            yield session

    def __del__(self):
        print('DELETE engine')
    # def __del__
