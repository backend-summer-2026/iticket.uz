from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.organizers.models import Organizer
from src.core.database import get_db, AsyncSession
from src.users.models import User
from src.users.service import UserService
from src.users.repository import UserRepository
from src.core.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
) -> User:
    """Hozirgi foydalanuvchini olish."""
    try:
        payload = decode_access_token(token)
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token noto'g'ri yoki muddati o'tgan",
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token noto'g'ri yoki muddati o'tgan",
        )

    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user = await user_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Foydalanuvchi topilmadi",
        )

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Hozirgi faol foydalanuvchini olish."""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Foydalanuvchi faol emas",
        )
    return current_user


async def get_current_active_superuser(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """Hozirgi faol superfoydalanuvchini olish."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Foydalanuvchi superfoydalanuvchi emas",
        )
    return current_user


async def get_current_orginization_user(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """Hozirgi faol tashkilot foydalanuvchini olish."""
    if not current_user.organizer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Foydalanuvchi organizer emas",
        )
    return current_user


async def get_current_orginizer(
    current_user: User = Depends(get_current_active_user), db: AsyncSession = Depends(get_db)
) -> Organizer:
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    organizer = await user_service.get_organizer_by_user_id(current_user.id)

    if not organizer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Foydalanuvchi organizer emas",
        )
    return organizer
