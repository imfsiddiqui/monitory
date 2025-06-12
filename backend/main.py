from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import uvicorn

app = FastAPI(
    title=settings.app.name,
    debug=settings.app.debug,
    version="0.1.0",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {
        "message": "Hello World",
        "app_name": settings.app.name,
        "environment": settings.app.environment,
        "debug": settings.app.debug,
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Example of using a secret value
@app.get("/secret")
async def get_secret():
    return {"secret_key": settings.security.secret_key}

@app.get("/config")
async def show_config():
    # Don't expose sensitive data in production!
    if settings.app.environment == "prod":
        return {"error": "Not available in production"}

    return {
        "database_url": str(settings.database.url),
        "redis_url": str(settings.cache.url) if settings.cache.url else None,
        "security": {
            "algorithm": settings.security.algorithm,
            "token_expire": settings.security.access_token_expire_minutes,
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.app.debug,
    )
