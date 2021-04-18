from typing import Optional
from pydantic import BaseModel, FilePath


class CoinBase(BaseModel):
    name: str


class CoinUpdate(BaseModel):
    name: Optional[str]
    logo: Optional[FilePath]


class CoinCreate(CoinBase):
    logo: Optional[FilePath]


class Coin(CoinBase):
    id: int
    logo: FilePath

    class Config:
        orm_mod = True
