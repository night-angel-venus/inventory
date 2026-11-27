from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models import User
from app.schemas import UserCreate, UserResponse, Token
from app.database import get_db
from app.api.exceptions import register_exception, login_exception
from sqlalchemy.orm import Session
from app.auth import (get_password_hash, verify_password, create_access_token)



router = APIRouter(prefix="/auth", tags=["Auth"])

db_dependency: Session = Depends(get_db)

@router.post("/register", response_model=UserResponse ,status_code=status.HTTP_201_CREATED)
def register(
    user: UserCreate,
    db = db_dependency
):

    existing_check = db.query(User).filter(User.username == user.username).first()

    if existing_check:
        raise register_exception

    hashed_password = get_password_hash(user.password)

    new_user = User(
        username = user.username,
        password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db = db_dependency
):
    user = db.query(User).filter(User.username == form_data.username).first()

    password = verify_password(form_data.password, user.password)

    if not user or not password:
        raise login_exception

    access_token = create_access_token(
        data = {"sub":user.username}
    )

    return {
        "access_token":access_token,
        "token_type": "bearer",
        "user":user
    }
    