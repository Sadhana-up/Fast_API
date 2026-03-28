from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DATABASE = "mysql+pymysql://root:my%40sql123@localhost:3306/new_schema"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,
                             autoflush=False, 
                             bind=engine) ## do mot commit automaticaly 
#autoflush : changes are not directly flushed without any need 
#bind : hamro main component is to bind 
# binded to the engine



Base = declarative_base() ## to create tables base is needed 
