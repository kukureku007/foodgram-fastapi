from dependency_injector import containers, providers

# TODO return some json empty result
from services.tags import TagService
from services.ingredients import IngredientService


class AppContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            'routers.ingredients',
            'routers.tags'
        ]
    )

    tag_service = providers.Factory(TagService)
    ingredient_service = providers.Factory(IngredientService)
