import ipaddress
import os
import socket

import nmap
from dotenv import load_dotenv

# Lê o backend/.env, onde podes definir REDE_ALVO (ex.: REDE_ALVO=192.168.1.0/24)
load_dotenv()


def obter_ip_local() -> str:
    # O connect em UDP não envia nada para a rede; só obriga o sistema
    # a escolher a interface de saída, e é assim que descobrimos o nosso IP.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ligacao:
        ligacao.connect(("8.8.8.8", 80))
        return ligacao.getsockname()[0]


def obter_rede_local(prefixo: int = 24) -> str:
    # Uma rede definida à mão tem sempre prioridade sobre a deteção automática,
    # porque com VPN ou hotspot o "IP de saída" não é o da rede de casa.
    rede_configurada = os.getenv("REDE_ALVO")
    if rede_configurada:
        return str(ipaddress.ip_network(rede_configurada, strict=False))

    rede = ipaddress.ip_network(f"{obter_ip_local()}/{prefixo}", strict=False)
    if not rede.is_private:
        raise ValueError(
            f"A rede detetada ({rede}) não é uma rede privada normal "
            "(192.168.x.x, 10.x.x.x ou 172.16-31.x.x). Pode ser VPN, hotspot ou uma "
            "rede gerida por outra entidade. Define a tua rede no backend/.env, "
            "por exemplo REDE_ALVO=192.168.1.0/24, e tenta de novo."
        )
    return str(rede)


def descobrir_dispositivos(rede: str | None = None) -> list[dict]:
    rede = rede or obter_rede_local()
    # Caminhos do instalador oficial no Windows: assim o scan funciona mesmo que
    # o terminal tenha sido aberto antes do Nmap ser instalado (PATH desatualizado).
    scanner = nmap.PortScanner(nmap_search_path=(
        "nmap",
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        r"C:\Program Files\Nmap\nmap.exe",
    ))
    # -sn = só descobre quem está ligado, sem varrer portas (rápido e discreto)
    scanner.scan(hosts=rede, arguments="-sn")

    dispositivos = []
    for ip in scanner.all_hosts():
        info = scanner[ip]
        mac = info["addresses"].get("mac")
        fabricante = info["vendor"].get(mac) if mac else None
        dispositivos.append({
            "ip": ip,
            "mac": mac,
            "nome": info.hostname() or None,
            "fabricante": fabricante,
            "tipo": None,
            "estado": "online" if info.state() == "up" else "offline",
        })
    return dispositivos
