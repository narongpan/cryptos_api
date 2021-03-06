from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel, Field, FilePath, condecimal

app = FastAPI()


class Cryptos(BaseModel):
    name: str
    logo: FilePath
    current_price_usd: condecimal(ge=0, decimal_places=9)
    last_price_usd_at: condecimal(ge=0, decimal_places=9)
    current_price_thb: condecimal(ge=0, decimal_places=9)
    last_price_thb_at: condecimal(ge=0, decimal_places=9)


@app.get("/cryptos/info")
def read_cryptos_info():
    return {
        "code": "0",
        "data": {
            "total_cryptos": 2,
            "cryptos": [
                {
                    "crypto_id": 1112,
                    "crypto_name": "BITCOIN",
                    "crypto_logo": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F9%2F9a%2FBTC_Logo.svg%2F2000px-BTC_Logo.svg.png&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ABTC_Logo.svg&tbnid=BR6Eemum0OA7IM&vet=12ahUKEwip67r9hIXwAhUTgGMGHazaDnwQMygAegUIARDYAQ..i&docid=awTjjYqsBYwGqM&w=2000&h=2000&q=btc%20logo&ved=2ahUKEwip67r9hIXwAhUTgGMGHazaDnwQMygAegUIARDYAQ",
                    "crypto_price": {
                        "current_price_usd": "2123.123456789",
                        "last_price_usd_at": "2014-10-15 18:36:05 +0700",
                        "current_price_thb": "2123.123456789",
                        "last_price_thb_at": "2014-10-15 18:36:05 +0700",
                    }
                },
                {
                    "crypto_id": 1113,
                    "crypto_name": "DODGE COIN",
                    "crypto_logo": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fd%2Fd0%2FDogecoin_Logo.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDogecoin&tbnid=D8T9XKPikDLASM&vet=12ahUKEwjEhISbhYXwAhVJsWMGHT8XAmYQMygBegUIARDSAQ..i&docid=ZssAvoh1tqNZoM&w=256&h=256&itg=1&q=doge%20logo&ved=2ahUKEwjEhISbhYXwAhVJsWMGHT8XAmYQMygBegUIARDSAQ",
                    "crypto_price": {
                        "current_price_usd": "2123.123456789",
                        "last_price_usd_at": "2014-10-15 18:36:05 +0700",
                        "current_price_thb": "2123.123456789",
                        "last_price_thb_at": "2014-10-15 18:36:05 +0700",
                    }
                }
            ]
        },
        "request_id": "0ba2887315178178017221014"
    }


@app.get("/orders")
def read_orders():
    return {
        "code": "0",
        "data": {
            "total_orders": 2,
            "orders": [
                {
                    "order_id": 1231233,
                    "transaction_number": "gus-1231l1l2n3",
                    "transaction_status": "MATCHED",  # MATCHED, CANCELED, PENDING
                    "coin_info": {
                        "crypto_id": 123,
                        "crypto_name": "BTC",
                        "qty": "12.123456789",
                        "current_price_usd": "2123.123456789",
                        "total_amount_usd": "1231123.123123123",
                        "current_price_thb": "2123.123456789",
                        "total_amount_thb": "123123.123123123",
                    },
                    "order_type": "BUY",  # BUY, SELL
                    "match_type": "LIMIT",  # LIMIT, STOP_LOSS, MARKET
                    "create_at": "",
                    "match_at": "",
                },
                {
                    "order_id": 1231234,
                    "transaction_number": "gus-1231l1l2n3",
                    "transaction_status": "MATCHED",  # MATCHED, CANCELED, PENDING
                    "coin_info": {
                        "crypto_id": 122,
                        "crypto_name": "BTC",
                        "qty": "12.123456789",
                        "current_price_usd": "2123.123456789",
                        "total_amount_usd": "1231123.123123123",
                        "current_price_thb": "2123.123456789",
                        "total_amount_thb": "123123.123123123",
                    },
                    "order_type": "BUY",  # BUY, SELL
                    "match_type": "LIMIT",  # LIMIT, STOP_LOSS, MARKET
                    "create_at": "",
                    "match_at": "",
                }
            ]
        },
        "request_id": "0ba2887315178178017221014"
    }


@app.get("/profile")
def read_profile():
    return {
        "code": "0",
        "data": {
                "user_id": 1231233,
                "user_first_name": "gus-1231l1l2n3",
                "user_last_name": "gus-1231l1l2n3",
                "user_telephone": "123123",
                "user_address": {
                    "address": "asdasdasdsad",
                    "province": "asdasd",
                    "zipcode": "123sad",
                    "country": "qweqwe"
                },
            "create_at": "",
            "last_update_at": "",
            "user_profile_image": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F9%2F9a%2FBTC_Logo.svg%2F2000px-BTC_Logo.svg.png&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ABTC_Logo.svg&tbnid=BR6Eemum0OA7IM&vet=12ahUKEwip67r9hIXwAhUTgGMGHazaDnwQMygAegUIARDYAQ..i&docid=awTjjYqsBYwGqM&w=2000&h=2000&q=btc%20logo&ved=2ahUKEwip67r9hIXwAhUTgGMGHazaDnwQMygAegUIARDYAQ",
            "user_wallet": {
                    "bank_id": "2123.123456789",
                    "bank_name": "",
                    "bank_account_name": "2123.123456789",
                    "bank_branch": "",
                    "wallet_balance": "",
                    "wallet_balance_at": ""
                }
        },
        "request_id": "0ba2887315178178017221014"
    }


@ app.get("/wallet/transactions")
def read_wallet_transactions():
    return {
        "code": "0",
        "data": [
            {
                "transaction_id": 1231233,
                "transaction_type": "DEPOSITE",  # WITHDRAW
                "deposite_info": {
                    "from_account": "123-1231-23123-",
                    "from_bank": "KASIKORN",
                },
                "withdraw_info": null,
                # "to_account": "",
                # "to_bank": "",
                "transaction_status": "COMPLETED",  # CANCELED
                "amount": "123.123123123123",
                "base_currency": "THB",
                "create_at": "",
                "complete_at": "",
                "canceled_at": ""
            }
        ]
    }


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@ app.put("/crypto/{crypto_id}")
def update_crypto(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@ app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@ app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
