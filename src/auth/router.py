from fastapi import APIRouter, Depends, HTTPException, status

from src.core.database import get_db, AsyncSession
from src.auth.schemas import UserRegisterRequest, UserLoginRequest, UserLoginResponse
from src.users.schemas import UserBase
from src.users.models import User
from src.users.service import UserService
from src.users.repository import UserRepository
from src.auth.dependencies import get_current_user  # type: ignore


router = APIRouter()


@router.post("/register", response_model=UserBase)
async def register_user(user: UserRegisterRequest, db: AsyncSession = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    created_user = await user_service.create_user(user)
    return created_user


@router.post("/login", response_model=UserLoginResponse)
async def login_user(user: UserLoginRequest, db: AsyncSession = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    existing_user = await user_service.get_user_by_email(user.email)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email yoki parol noto'g'ri",
        )

    # Parolni tekshirish
    if not user_service.verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email yoki parol noto'g'ri",
        )

    # Token yaratish (JWT yoki boshqa usul bilan)
    token = user_service.create_access_token(existing_user.id)

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserBase)
async def get_current_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user
