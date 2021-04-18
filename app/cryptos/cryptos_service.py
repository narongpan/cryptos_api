from typing import List
from uuid import uuid4
from app.cryptos.dto import Crypto


class CryptosService:
    def __init__(self, cryptos: List[Crypto]) -> None:
        self.cryptos = cryptos

    def find_all(self) -> List[Crypto]:
        return self.cryptos

    def find_one(self, id: str) -> Crypto:
        return next((crypto for crypto in self.cryptos if crypto["id"] == id), None)

    def create(self, crypto: Crypto) -> Crypto:
        id = uuid4().hex
        crypto_dict = crypto.dict()
        crypto_dict["id"] = id
        self.cryptos.append(crypto_dict)
        found_crypto = self.find_one(id)

        return found_crypto

    def update(self, id: str, crypto: Crypto) -> Crypto:
        found_crypto = self.find_one(id)

        if found_crypto is None:
            return None

        model = Crypto(**found_crypto)
        update_data = crypto.dict(exclude_unset=True)
        updated_crypto = model.copy(update=update_data)
        index = self.cryptos.index(found_crypto)
        self.cryptos[index] = updated_crypto

        return updated_crypto

    def delete(self, id: str) -> Crypto:
        found_crypto = self.find_one(id)

        if found_crypto is None:
            return None

        index = self.cryptos.index(found_crypto)
        deleted_crypto = self.cryptos.pop(index)

        return deleted_crypto
