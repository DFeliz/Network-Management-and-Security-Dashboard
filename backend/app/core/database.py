import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

URL_BASE_DADOS = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/network_dashboard"
)

motor = create_engine(URL_BASE_DADOS)
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)


class Base(DeclarativeBase):
    pass


def obter_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()
