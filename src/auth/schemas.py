from typing import Self

from pydantic import BaseModel, EmailStr, Field, model_validator


class UserRegisterRequest(BaseModel):
    """Foydalanuvchi ro'yxatdan o'tish uchun so'rov modeli."""

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    confirm_password: str = Field(min_length=8, max_length=128)

    @model_validator(mode="after")
    def validate_passwords(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


class UserLoginRequest(BaseModel):
    """Foydalanuvchi tizimga kirish uchun so'rov modeli."""

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserLoginResponse(BaseModel):
    """Foydalanuvchi tizimga kirish uchun javob modeli."""

    access_token: str
    token_type: str = "bearer"
