from dependency_injector import containers, providers

# TODO return some json empty result
# TODO refactor to multicontainers

from repositories.sqlalchemy_repo.db import Database

from repositories.sqlalchemy_repo.tags import TagRepository
from repositories.sqlalchemy_repo.ingredients import IngredientRepository

from services.tags import TagService
from services.ingredients import IngredientService


class AppContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            'routers',
        ],
    )
    #     modules=[
    #         'routers.ingredients',
    #         'routers.tags'
    #     ]

    database = providers.Singleton(Database)

    tag_repository = providers.Factory(
        TagRepository,
        async_session_factory=database.provided.async_session
    )
    ingredient_repository = providers.Factory(
        IngredientRepository,
        async_session_factory=database.provided.async_session
    )

    tag_service = providers.Factory(
        TagService,
        tag_repository=tag_repository
    )
    ingredient_service = providers.Factory(
        IngredientService,
        ingredient_repository=ingredient_repository
    )
