from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import FilePath


class WalletBase(BaseModel):
    name: str


class WalletCreate(WalletBase):
    pass


class Wallet(WalletBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    hashed_passwod: str
    wallet: Wallet

    class Config:
        orm_mode = True
