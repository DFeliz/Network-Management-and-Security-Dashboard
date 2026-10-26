from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.devices import router as router_dispositivos
from app.core.database import Base, motor
from app.models import dispositivo  # noqa: F401 - regista o modelo

app = FastAPI(
    title="Network Management and Security Dashboard",
    description="API para gestão e monitorização de uma rede.",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas na base de dados ao iniciar
Base.metadata.create_all(bind=motor)

app.include_router(router_dispositivos)


@app.get("/")
def inicio():
    return {
        "mensagem": "API do Network Management and Security Dashboard a funcionar!",
        "status": "online"
    }


@app.get("/health")
def verificar_estado():
    return {"status": "ok"}
