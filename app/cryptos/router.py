from .dtos import CoinCreate, CoinUpdate
from dotenv import load_dotenv
import os
from fastapi import APIRouter
from .cryptos_repository_mongo import CryptosRepositoryMongo
from .cryptos_repository_postgres import CryptosRepositoryPostgres
from .cryptos_service import CryptosService
from helpers import make_response
from database.nosql import mongo
from database.sql import postgres

load_dotenv()
db_provider = os.getenv("DB_PROVIDER")
cryptos_repo = None

print("db_provider: " + db_provider)


if db_provider == "mongo":
    cryptos_repo = CryptosRepositoryMongo(
        mongo.db.get_collection('cryptos', codec_options=mongo.codec_options)
    )
elif db_provider == "postgres":
    cryptos_repo = CryptosRepositoryPostgres(postgres.SessionLocal())
else:
    raise Exception("Database provider could not be found from the env var.")

cryptos_service = CryptosService(cryptos_repo)
router = APIRouter()


@router.get("/")
async def read_cryptos_info():
    print("HElloo")
    return make_response("cryptos", await cryptos_service.find_all())


@router.get("/{crypto_id}")
async def get_crypto(crypto_id: str):
    return make_response("crypto", await cryptos_service.find_one(crypto_id))


@router.post("/", status_code=201)
async def create_cryptos_info(crypto_info: CoinCreate):
    return make_response("crypto", await cryptos_service.create(crypto_info))


@router.patch("/{crypto_id}")
async def update_cryptos_info(crypto_id: str, crypto_info: CoinUpdate):
    return make_response("crypto", await cryptos_service.update(crypto_id, crypto_info))


@router.delete("/{crypto_id}", status_code=204)
async def delete_crypto(crypto_id: str):
    result = await cryptos_service.delete(crypto_id)

    if result == 0:
        return make_response("crypto", None)

    return make_response("crypto", crypto_id)
