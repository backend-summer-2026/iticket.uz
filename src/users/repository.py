from typing import Any

from src.core.database import AsyncSession
from sqlalchemy import select

from src.users.models import User
from src.users.schemas import UserBase


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_user_by_id(self, user_id: str) -> Any | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def get_user_by_email(self, email: str) -> Any | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    async def create_user(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update_user(self, user: User) -> User:
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, user: User) -> None:
        # FIXME: delete qilinganda inactive qilinishi kerak, shunchaki o'chirib yuborish emas
        await self.session.delete(user)
        await self.session.commit()
