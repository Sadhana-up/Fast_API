from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import make_url

from app.core.database import Base, engine, SQLALCHEMY_DATABASE_URL
from app.db.models import user


def ensure_database_exists():
    url = make_url(SQLALCHEMY_DATABASE_URL)

    if not url.drivername.startswith("mysql"):
        return

    database_name = url.database
    if not database_name:
        return

    server_url = url.set(database="")
    server_engine = create_engine(server_url)

    try:
        with server_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{database_name}`"))
            conn.commit()
    finally:
        server_engine.dispose()


def create_tables():
    ensure_database_exists()
    Base.metadata.create_all(bind=engine)
    