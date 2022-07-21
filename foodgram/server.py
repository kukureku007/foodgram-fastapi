from fastapi import FastAPI
import routers

# uvicorn server:app --reload --port 8000
app = FastAPI()
app.include_router(routers.tags_router)
app.include_router(routers.ingredient_router)
