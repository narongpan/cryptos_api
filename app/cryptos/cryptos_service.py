from repository import Repository
from typing import List
from app.cryptos.dto import Crypto


class CryptosService:
    def __init__(self, cryptos_repository: Repository) -> None:
        self.cryptos_repository = cryptos_repository

    async def find_all(self) -> List[Crypto]:
        return self.cryptos_repository.find_all()

    async def find_one(self, id: str) -> Crypto:
        return self.cryptos_repository.find_one(id)

    async def create(self, crypto: Crypto) -> Crypto:
        return self.cryptos_repository.create(crypto)

    async def update(self, id: str, crypto: Crypto) -> Crypto:
        return self.cryptos_repository.update(id, crypto)

    async def delete(self, id: str) -> int:
        return self.cryptos_repository.delete(id)
