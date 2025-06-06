from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.auth.jwt import verify_token

def get_current_user(db: Session = Depends(get_db), token: str = Depends(verify_token)) -> User:
    user = db.query(User).filter(User.id == token.user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
