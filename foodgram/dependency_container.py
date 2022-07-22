from dependency_injector import containers, providers

# TODO return some json empty result

from repositories.sqlalchemy_repo.tags import TagRepository
from repositories.sqlalchemy_repo.ingredients import IngredientRepository

from services.tags import TagService
from services.ingredients import IngredientService


class AppContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            'routers.ingredients',
            'routers.tags'
        ]
    )

    tag_repository = providers.Factory(TagRepository)
    ingredient_repository = providers.Factory(IngredientRepository)

    tag_service = providers.Factory(
        TagService,
        tag_repository=tag_repository
    )
    ingredient_service = providers.Factory(
        IngredientService,
        ingredient_repository=ingredient_repository
    )
