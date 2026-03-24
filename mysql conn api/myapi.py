from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel
from typing import List,   Optional
