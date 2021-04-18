from bson import ObjectId
from repository import Repository
from typing import List
from app.cryptos.dto import CreateCryptoDTO, Crypto, UpdateCryptoDTO


def transform_result(result):
    print("result:")
    print(result)
    return {
        "id": str(result["_id"]),
        "name": result["name"],
        "logo": result["logo"],
        "current_price_usd": result["current_price_usd"],
        "last_price_usd_at": result["last_price_usd_at"],
        "current_price_thb": result["current_price_thb"],
        "last_price_thb_at": result["last_price_thb_at"],

    }


class CryptosRepositoryMongo(Repository):
    def __init__(self, cryptosCollection) -> None:
        self.collection = cryptosCollection

    async def find_all(self) -> List[Crypto]:
        print("CryptosRepositoryMongo.find_all()")
        cryptos = []

        async for crypto in self.collection.find():
            cryptos.append(transform_result(crypto))

        return cryptos

    async def find_one(self, id: str) -> Crypto:
        found = await self.collection.find_one({"_id": ObjectId(id)})

        return transform_result(found)

    async def create(self, create_dto: CreateCryptoDTO):
        print("CryptosRepositoryMongo.create()")
        created = await self.collection.insert_one(create_dto.dict())
        print("created:")
        print(created)
        found = await self.collection.find_one({"_id": ObjectId(created.inserted_id)})
        print("found:")
        print(found)

        return transform_result(found)

    async def update(self, id: str, update_dto: UpdateCryptoDTO) -> Crypto:
        update_dict = update_dto.dict()

        if len(update_dict) < 1:
            return None

        update_result = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_dict})

        if update_result:
            found = await self.find_one(id)

            return found

        return None

    async def delete(self, id: str):
        delete_result = await self.collection.delete_one({"_id": ObjectId(id)})

        if delete_result.deleted_count == 1:
            return id

        return False
