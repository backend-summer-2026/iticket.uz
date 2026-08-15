import jwt
from passlib.context import CryptContext

from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Parolni hash qilish."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Parolni tekshirish."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: str) -> str:
    """JWT token yaratish."""
    payload = {"user_id": user_id}
    token = jwt.encode(payload, "your_secret_key", algorithm="HS256")
    return token


def decode_access_token(token: str) -> dict:
    """JWT tokenni dekodlash."""
    try:
        payload = jwt.decode(token, "your_secret_key", algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token noto'g'ri yoki muddati o'tgan",
        )
