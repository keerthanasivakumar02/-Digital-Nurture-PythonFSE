from passlib.context import CryptContext

# bcrypt is preferred because it is intentionally slow,
# making brute-force attacks much harder than MD5 or SHA-256,
# which are designed to be fast.

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )