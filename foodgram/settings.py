import os
from dotenv import load_dotenv

# TODO: change to pathlib
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(__file__)
# print(BASE_DIR)

load_dotenv(f'{BASE_DIR}/../infra/.env')

POSTGRES_USER = os.getenv('POSTGRES_USER', default='')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='')
POSTGRES_HOST = os.getenv('DB_HOST', default='')
POSTGRES_PORT = os.getenv('DB_PORT', default='')
POSTGRES_DATABASE_NAME = os.getenv('DB_NAME', default='')


# TODO config for engine 
DATABASE_URL = (
    f'postgresql+asyncpg://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/'
    f'{POSTGRES_DATABASE_NAME}'
)

# TODO Alembic returns errors on async
DATABASE_URL_SYNC = (
    f'postgresql://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/'
    f'{POSTGRES_DATABASE_NAME}'
)