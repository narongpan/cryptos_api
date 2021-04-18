from fastapi import APIRouter
from app.cryptos.cryptos_service import CryptosService
from app.cryptos.dto import CreateCryptoDTO, UpdateCryptoDTO
from helpers import make_response
from db import db

cryptos_service = CryptosService(db["cryptos"])
router = APIRouter()


@router.get("/")
def read_cryptos_info():
    return make_response("cryptos", cryptos_service.find_all())


@router.get("/{crypto_id}")
def get_crypto(crypto_id: str):
    return make_response("crypto", cryptos_service.find_one(crypto_id))


@router.post("/", status_code=201)
def create_cryptos_info(crypto_info: CreateCryptoDTO):
    return make_response("crypto", cryptos_service.create(crypto_info))


@router.patch("/{crypto_id}")
def update_cryptos_info(crypto_id: str, crypto_info: UpdateCryptoDTO):
    return make_response("crypto", cryptos_service.update(crypto_id, crypto_info))


@router.delete("/{crypto_id}", status_code=204)
def delete_crypto(crypto_id: str):
    return make_response("crypto", cryptos_service.delete(crypto_id))
