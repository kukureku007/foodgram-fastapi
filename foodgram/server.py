from fastapi import FastAPI

import routers
from dependency_container import AppContainer

# uvicorn server:app --reload --port 8000
app_container = AppContainer()
app = FastAPI()
app.app_container = app_container
app.include_router(routers.tags_router)
app.include_router(routers.ingredient_router)
app.include_router(routers.additional_router)
