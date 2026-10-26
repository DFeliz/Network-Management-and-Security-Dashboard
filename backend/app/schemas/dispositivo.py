from pydantic import BaseModel


class DispositivoBase(BaseModel):
    ip: str
    mac: str
    nome: str | None = None
    fabricante: str | None = None
    tipo: str | None = None
    estado: str = "offline"


class DispositivoCriar(DispositivoBase):
    pass


class DispositivoResposta(DispositivoBase):
    id: int

    model_config = {"from_attributes": True}
