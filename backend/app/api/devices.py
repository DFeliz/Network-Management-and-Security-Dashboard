import os

from fastapi import APIRouter, Depends, HTTPException
from nmap import PortScannerError
from sqlalchemy.orm import Session

from app.core.database import obter_db
from app.models.dispositivo import Dispositivo
from app.schemas.dispositivo import DispositivoResposta, DispositivoCriar
from app.services.descoberta import descobrir_dispositivos, obter_rede_local
from app.services.sincronizacao import atualizar_dispositivos_na_base

router = APIRouter(
    prefix="/devices",
    tags=["Dispositivos"]
)


@router.get("/", response_model=list[DispositivoResposta])
def obter_dispositivos(db: Session = Depends(obter_db)):
    # Sem ORDER BY o PostgreSQL devolve as linhas por ordem física, que muda
    # depois de cada UPDATE (o scan); ordenar por id mantém a tabela estável.
    return db.query(Dispositivo).order_by(Dispositivo.id).all()


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


# Função normal (sem async) de propósito: o FastAPI corre-a numa thread à parte,
# por isso o scan, que demora segundos, não bloqueia o resto da API.
@router.post("/scan")
def scan_agora(db: Session = Depends(obter_db)):
    # A rede vem da configuração do servidor (REDE_ALVO no .env) e nunca do pedido,
    # para que ninguém consiga usar esta API para varrer redes alheias.
    # O scan nunca escolhe a rede sozinho: a deteção automática pode apanhar uma VPN
    # ou uma rede de escola/empresa que não é tua. A rede tem de ser declarada.
    if not os.getenv("REDE_ALVO"):
        raise HTTPException(
            status_code=400,
            detail="Define a rede a analisar no backend/.env, por exemplo "
                   "REDE_ALVO=192.168.1.0/24, e reinicia a API.",
        )

    try:
        rede = obter_rede_local()
        encontrados = descobrir_dispositivos(rede)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    except PortScannerError as erro:
        raise HTTPException(status_code=500, detail=f"Falha ao executar o Nmap: {erro}")

    resultado = atualizar_dispositivos_na_base(db, encontrados)
    resultado["rede"] = rede
    return resultado
