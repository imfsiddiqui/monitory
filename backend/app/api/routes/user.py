from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user_by_email
from app.auth.jwt import create_access_token
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await create_user(user)
    return new_user

@router.post("/login")
async def login_user(user: UserCreate):
    db_user = await get_user_by_email(user.email)
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(sub=db_user.email)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def read_me(current_user: UserResponse = Depends(get_current_active_user)):
    return current_user
