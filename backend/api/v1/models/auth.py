from typing import Optional, List

from flask_jwt_extended import create_access_token, create_refresh_token
from pydantic import BaseModel, validator, ValidationError

from backend.db.models import UserModel


class LoginInputDTO(BaseModel):
    login: str
    password: str


class AuthIdentityDTO(BaseModel):
    @classmethod
    def from_model(cls, model: UserModel):
        if model is None:
            return cls(login="", email="", id=-1)
        return cls(
            login=model.login,
            email=model.email,
            id=model.id,
        )

    login: str
    email: Optional[str]
    id: int


class AuthDataDTO(BaseModel):
    @classmethod
    def from_model(cls, model: UserModel):
        if model is None:
            return cls(
                access_token="",
                refresh_token="",
                identity=AuthIdentityDTO(None),
            )
        return cls(
            access_token=create_access_token(
                model.id
            ),
            refresh_token=create_refresh_token(
                model.id
            ),
            identity=AuthIdentityDTO.from_model(model),
        )

    access_token: str
    refresh_token: str
    identity: AuthIdentityDTO


class RegistrationInputDTO(BaseModel):
    login: str
    email: str = None
    password: str

    @validator("password")
    def correct_length(cls, v):
        if len(v) < 6:
            raise ValidationError("Пароль должен быть длиннее 6 символов")
        return v


class ResetInputDTO(BaseModel):
    login: str
    password: str

    @validator("password")
    def correct_length(cls, v):
        if len(v) < 6:
            raise ValidationError("Пароль должен быть длиннее 6 символов")
        return v
