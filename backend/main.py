from fastapi import FastAPI

app = FastAPI(
    title="Network Management and Security Dashboard",
    description="Painel de Gestão e Segurança de Rede",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "mensagem": "API do Network Management and Security Dashboard a funcionar!",
        "status": "online"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}