from fastapi import APIRouter

router = APIRouter(
    prefix="/devices",
    tags=["Dispositivos"]
)

devices = [
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
    return devices


@router.get("/{device_id}")
def obter_dispositivo(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            return device

    return {"erro": "Dispositivo não encontrado"}