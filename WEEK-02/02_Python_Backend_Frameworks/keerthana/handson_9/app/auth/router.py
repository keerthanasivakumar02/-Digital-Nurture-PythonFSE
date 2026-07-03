from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas import UserRegister, UserLogin
from app.database import users

from app.auth.security import (
    get_password_hash,
    verify_password
)

from app.auth.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register/")
def register(user: UserRegister):

    # Check if email already exists
    for existing_user in users:

        if existing_user["email"] == user.email:

            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

    # Hash password before storing
    hashed_password = get_password_hash(
        user.password
    )

    new_user = {
        "id": len(users) + 1,
        "email": user.email,
        "hashed_password": hashed_password,
        "is_active": True
    }

    users.append(new_user)

    return {
        "message": "User registered successfully"
    }


@router.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    for existing_user in users:

        if existing_user["email"] == form_data.username:

            if verify_password(
                form_data.password,
                existing_user["hashed_password"]
            ):

                token = create_access_token(
                    {
                        "sub": existing_user["email"]
                    }
                )

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )