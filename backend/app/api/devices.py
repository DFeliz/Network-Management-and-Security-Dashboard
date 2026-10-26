from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import obter_db
from app.models.dispositivo import Dispositivo
from app.schemas.dispositivo import DispositivoResposta, DispositivoCriar

router = APIRouter(
    prefix="/devices",
    tags=["Dispositivos"]
)


@router.get("/", response_model=list[DispositivoResposta])
def obter_dispositivos(db: Session = Depends(obter_db)):
    return db.query(Dispositivo).all()


@router.get("/{id_dispositivo}", response_model=DispositivoResposta)
def obter_dispositivo(id_dispositivo: int, db: Session = Depends(obter_db)):
    dispositivo = db.query(Dispositivo).filter(Dispositivo.id == id_dispositivo).first()
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
    return dispositivo


@router.post("/", response_model=DispositivoResposta)
def criar_dispositivo(dados: DispositivoCriar, db: Session = Depends(obter_db)):
    dispositivo = Dispositivo(**dados.model_dump())
    db.add(dispositivo)
    db.commit()
    db.refresh(dispositivo)
    return dispositivo
