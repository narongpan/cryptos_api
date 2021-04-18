from repository import Repository
from typing import List
from app.cryptos.dto import Crypto


class CryptosService:
    def __init__(self, cryptos_repository: Repository) -> None:
        self.cryptos_repository = cryptos_repository

    def find_all(self) -> List[Crypto]:
        return self.cryptos_repository.find_all()

    def find_one(self, id: str) -> Crypto:
        return self.cryptos_repository.find_one(id)

    def create(self, crypto: Crypto) -> Crypto:
        return self.cryptos_repository.create(crypto)

    def update(self, id: str, crypto: Crypto) -> Crypto:
        return self.cryptos_repository.update(id, crypto)

    def delete(self, id: str) -> Crypto:
        return self.cryptos_repository.delete(id)
