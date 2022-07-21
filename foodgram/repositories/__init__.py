class BaseRepository:
    async def create(self):
        raise NotImplementedError

    async def read(self):
        raise NotImplementedError

    async def read_all(self):
        raise NotImplementedError

    async def update(self):
        raise NotImplementedError

    async def delete(self):
        raise NotImplementedError

    def __make_filters__(self):
        raise NotImplementedError
