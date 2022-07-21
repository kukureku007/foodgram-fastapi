from functools import wraps
from models import BaseAPIModel


def handle_response(output_model: BaseAPIModel):
    """
    transform result from orm to pydentic
    """
    def decorator(func):
        # TODO get output model from annotation
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # print(func.__annotations__)
            result = await func(*args, **kwargs)

            if isinstance(result, list):
                return [output_model.from_orm(x) for x in result]

            if not result:
                return None
            return output_model.from_orm(result)

        return wrapper
    return decorator
