import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

URL_BASE_DADOS = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:password@localhost:5432/network_dashboard"
)

# Garante que usa psycopg2 se a URL vier só com postgresql://
if URL_BASE_DADOS.startswith("postgresql://"):
    URL_BASE_DADOS = URL_BASE_DADOS.replace("postgresql://", "postgresql+psycopg2://", 1)

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
