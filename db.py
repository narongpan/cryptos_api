import os
from dotenv import load_dotenv
from decimal import Decimal
from bson.codec_options import CodecOptions, TypeCodec, TypeRegistry
from bson.decimal128 import Decimal128
import motor.motor_asyncio

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if MONGO_URL is None:
    raise Exception("MongoDB URL could not be found from  the env var.")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.bitgus


class DecimalCodec(TypeCodec):
    python_type = Decimal
    bson_type = Decimal128

    def transform_python(self, value):
        return Decimal128(value)

    def transform_bson(self, value):
        return value.to_decimal()


decimal_codec = DecimalCodec()
type_registry = TypeRegistry([decimal_codec])
codec_options = CodecOptions(type_registry=type_registry)
