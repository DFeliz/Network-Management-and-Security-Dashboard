from fastapi import APIRouter

router = APIRouter(
    prefix="/devices",
    tags=["Dispositivos"]
)

dispositivos = [
    {
        "id": 1,
        "ip": "192.168.1.10",
        "mac": "AA:BB:CC:DD:EE:01",
        "nome": "PC",
        "fabricante": "Intel",
        "tipo": "Computador",
        "estado": "online"
    },
    {
        "id": 2,
        "ip": "192.168.1.11",
        "mac": "AA:BB:CC:DD:EE:02",
        "nome": "Telemóvel",
        "fabricante": "Samsung",
        "tipo": "Telemóvel",
        "estado": "online"
    },
    {
        "id": 3,
        "ip": "192.168.1.12",
        "mac": "AA:BB:CC:DD:EE:03",
        "nome": "Impressora",
        "fabricante": "HP",
        "tipo": "Impressora",
        "estado": "offline"
    }
]


@router.get("/")
def obter_dispositivos():
    return dispositivos


@router.get("/{id_dispositivo}")
def obter_dispositivo(id_dispositivo: int):
    for dispositivo in dispositivos:
        if dispositivo["id"] == id_dispositivo:
            return dispositivo

    return {"erro": "Dispositivo não encontrado"}
