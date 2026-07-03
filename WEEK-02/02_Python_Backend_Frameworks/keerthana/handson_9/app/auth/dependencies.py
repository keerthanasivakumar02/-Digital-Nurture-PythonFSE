from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.database import users
from app.auth.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_access_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    email = payload.get("sub")

    for user in users:

        if user["email"] == email:
            return user

    raise HTTPException(
        status_code=401,
        detail="User not found"
    )