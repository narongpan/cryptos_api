from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

postgres_url = os.getenv("POSTGRES_URL")

if postgres_url is None:
    raise Exception(
        "Postgres connection URL could not be found from the env var.")

engine = create_engine(postgres_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
