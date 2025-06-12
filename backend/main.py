from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import uvicorn

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {
        "message": "Hello World",
        "app_name": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug,
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Example of using a secret value
@app.get("/secret")
async def get_secret():
    return {"secret_key": settings.secret_key}

@app.get("/config")
async def show_config():
    # Don't expose sensitive data in production!
    if settings.environment == "prod":
        return {"error": "Not available in production"}

    return {
        "database_url": str(settings.database_url),
        "redis_url": str(settings.redis_url) if settings.redis_url else None,
        "security": {
            "algorithm": settings.algorithm,
            "token_expire": settings.access_token_expire_minutes,
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
