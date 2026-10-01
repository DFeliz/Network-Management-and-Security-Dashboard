from fastapi import FastAPI
from app.api.devices import router as devices_router

app = FastAPI(
    title="Network Management and Security Dashboard",
    description="API para gestão e monitorização de uma rede.",
    version="0.1.0"
)

app.include_router(devices_router)

@app.get("/")
def inicio():
    return {
        "mensagem": "API do Network Management and Security Dashboard a funcionar!",
        "status": "online"
    }

@app.get("/health")
def verificar_estado():
    return {"status": "ok"}