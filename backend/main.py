from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Default FastAPI App"),  # Default value if not set
    debug=os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
)

@app.get("/")
async def read_root():
    return {
        "message": "Hello World",
        "app_name": os.getenv("APP_NAME"),
        "debug_mode": os.getenv("DEBUG")
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Example of using a secret value
@app.get("/secret")
async def get_secret():
    return {"secret_key": os.getenv("SECRET_KEY")}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),  # Default to 8000 if not set
        reload=os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    )
