from database.sql.models import Coin
from database.sql.schemas import CoinCreate, CoinUpdate
from repository import Repository


class CryptosRepositoryPostgres(Repository):
    def __init__(self, postgres_session) -> None:
        self.db = postgres_session

    async def find_all(self):
        return self.db.query(Coin).all()

    async def find_one(self, id):
        return self.db.query(Coin).filter(Coin.id == id).first()

    async def create(self, dto: CoinCreate):
        coin = Coin(**dto.dict())

        self.db.add(coin)
        self.db.commit()
        self.db.refresh(coin)

        return coin

    async def update(self, id, dto: CoinUpdate):
        coin = Coin(**dto.dict())
        result = self.db.query(Coin).filter(Coin.id == id).update(
            dto.dict(), synchronize_session="fetch")

        self.db.commit()

        print("result: {}".format(result))

        if result == 0:
            return None

        return coin

    async def delete(self, id) -> int:
        result = self.db.query(Coin).filter(Coin.id == id).delete()

        self.db.commit()

        return result
