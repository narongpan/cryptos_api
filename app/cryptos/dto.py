from typing import Optional
from pydantic import BaseModel, FilePath, condecimal


class CreateCryptoDTO(BaseModel):
    name: str
    logo: Optional[FilePath] = None
    current_price_usd: condecimal(ge=0, decimal_places=9)
    last_price_usd_at: condecimal(ge=0, decimal_places=9)
    current_price_thb: condecimal(ge=0, decimal_places=9)
    last_price_thb_at: condecimal(ge=0, decimal_places=9)


class UpdateCryptoDTO(BaseModel):
    name: Optional[str]
    log: Optional[FilePath]
    current_price_usd: Optional[condecimal(ge=0, decimal_places=9)]
    last_price_usd_at: Optional[condecimal(ge=0, decimal_places=9)]
    current_price_thb: Optional[condecimal(ge=0, decimal_places=9)]
    last_price_thb_at: Optional[condecimal(ge=0, decimal_places=9)]


class Crypto(CreateCryptoDTO):
    id: str
