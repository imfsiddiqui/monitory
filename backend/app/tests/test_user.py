from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.models.user import User
from app.crud.user import create_user
from app.schemas.user import UserCreate

app = FastAPI()

client = TestClient(app)

def test_create_user():
    user_data = UserCreate(username="testuser", email="test@example.com", password="password")
    response = client.post("/users/", json=user_data.model_dump())
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["username"] == user_data.username
    assert created_user["email"] == user_data.email

def test_get_user():
    response = client.get("/users/testuser/")
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == "testuser"

def test_create_user_duplicate():
    user_data = UserCreate(username="testuser", email="test@example.com", password="password")
    response = client.post("/users/", json=user_data.model_dump())
    assert response.status_code == 400  # Assuming duplicate username returns 400

def test_delete_user():
    response = client.delete("/users/testuser/")
    assert response.status_code == 204  # Assuming successful deletion returns 204

def test_get_nonexistent_user():
    response = client.get("/users/nonexistent/")
    assert response.status_code == 404  # Assuming non-existent user returns 404
