from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ip: Mapped[str] = mapped_column(String(45), nullable=False)
    mac: Mapped[str] = mapped_column(String(17), nullable=False, unique=True)
    nome: Mapped[str | None] = mapped_column(String(100), nullable=True)
    fabricante: Mapped[str | None] = mapped_column(String(100), nullable=True)
    tipo: Mapped[str | None] = mapped_column(String(50), nullable=True)
    estado: Mapped[str] = mapped_column(String(20), default="offline")
