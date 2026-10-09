from fastapi import FastAPI
from app.api.devices import router as router_dispositivos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Network Management and Security Dashboard",
    description="API para gestão e monitorização de uma rede.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
