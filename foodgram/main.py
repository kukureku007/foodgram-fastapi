import os
import sys
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from dotenv import load_dotenv

# путь к файлу main - перейдёт в настройки
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(__file__)
# print(BASE_DIR)

load_dotenv(f'{BASE_DIR}/../.env')


# TODO: env file
POSTGRES_USER = os.getenv('POSTGRES_USER', default='')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='')
POSTGRES_HOST = os.getenv('DB_HOST', default='')
POSTGRES_PORT = os.getenv('DB_PORT', default='')
POSTGRES_DATABASE_NAME = os.getenv('DB_NAME', default='')

databse_url = (
    f'postgresql://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/'
    f'{POSTGRES_DATABASE_NAME}'
)

# to startapp check if no - create database and migrate - maybe..
# if no - raise error - no database
if not database_exists(databse_url):
    print('creating database')
    create_database(databse_url)

if __name__=='__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'drop_database':
            drop_database(databse_url)

# models - sqlalchemy models
# schemas - pydentic
