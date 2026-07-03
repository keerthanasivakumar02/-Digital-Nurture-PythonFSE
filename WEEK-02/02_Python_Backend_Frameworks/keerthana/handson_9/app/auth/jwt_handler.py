from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "mysecretkey123"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None
# OAuth2 Authorization Code Flow:
# In the Authorization Code Flow, the user logs in through an authorization server.
# The client application receives an authorization code, exchanges it for an access token,
# and then uses the token to access protected APIs.
#
# This project uses the OAuth2 Password Flow with JWT:
# The user sends username and password directly to the API.
# After successful authentication, the API generates a JWT access token.
# The client includes the JWT in the Authorization header (Bearer token)
# to access protected endpoints.