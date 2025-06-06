from fastapi import FastAPI
from app.api.routes import user as user_routes
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(user_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
