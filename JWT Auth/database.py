import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

URL_DATABASE = os.getenv("URL_DATABASE")
if not URL_DATABASE:
    raise ValueError("URL_DATABASE is not set. Add it to JWT Auth/.env")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,
                             autoflush=False, 
                             bind=engine) 

Base = declarative_base() 

