from app.cryptos.cryptos_repository_mongo import CryptosRepositoryMongo
from fastapi import APIRouter
from app.cryptos.cryptos_service import CryptosService
from app.cryptos.dto import CreateCryptoDTO, UpdateCryptoDTO
from helpers import make_response
from db import db, codec_options

cryptos_repository_mongo = CryptosRepositoryMongo(
    db.get_collection('cryptos', codec_options=codec_options))
cryptos_service = CryptosService(cryptos_repository_mongo)
router = APIRouter()


@router.get("/")
async def read_cryptos_info():
    print("HElloo")
    return make_response("cryptos", await cryptos_service.find_all())


@router.get("/{crypto_id}")
async def get_crypto(crypto_id: str):
    return make_response("crypto", await cryptos_service.find_one(crypto_id))


@router.post("/", status_code=201)
async def create_cryptos_info(crypto_info: CreateCryptoDTO):
    return make_response("crypto", await cryptos_service.create(crypto_info))


@router.patch("/{crypto_id}")
async def update_cryptos_info(crypto_id: str, crypto_info: UpdateCryptoDTO):
    return make_response("crypto", await cryptos_service.update(crypto_id, crypto_info))


@router.delete("/{crypto_id}", status_code=204)
async def delete_crypto(crypto_id: str):
    result = await cryptos_service.delete(crypto_id)

    if result is False:
        return make_response("crypto", None)

    return make_response("crypto", crypto_id)
