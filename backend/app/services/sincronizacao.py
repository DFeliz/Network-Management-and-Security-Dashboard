from sqlalchemy.orm import Session

from app.models.dispositivo import Dispositivo


def atualizar_dispositivos_na_base(db: Session, encontrados: list[dict]) -> dict:
    """Junta o resultado de um scan com o que já está na tabela dispositivos."""
    macs_encontrados = set()
    novos = 0
    atualizados = 0
    ignorados_sem_mac = 0

    for item in encontrados:
        mac = (item["mac"] or "").upper()
        if not mac:
            # A coluna mac é obrigatória e única, e é ela que identifica o aparelho
            # (o IP muda com o DHCP, o MAC não). Sem MAC não dá para o distinguir;
            # acontece com o próprio PC, que o Nmap não resolve.
            ignorados_sem_mac += 1
            continue

        macs_encontrados.add(mac)
        nome = item["nome"][:100] if item["nome"] else None
        fabricante = item["fabricante"][:100] if item["fabricante"] else None

        dispositivo = db.query(Dispositivo).filter(Dispositivo.mac == mac).first()
        if dispositivo is None:
            db.add(Dispositivo(
                mac=mac,
                ip=item["ip"],
                nome=nome,
                fabricante=fabricante,
                tipo=item["tipo"],
                estado="online",
            ))
            novos += 1
        else:
            dispositivo.ip = item["ip"]
            dispositivo.estado = "online"
            # Um scan que não descobriu o nome não pode apagar um nome já preenchido
            if nome:
                dispositivo.nome = nome
            if fabricante:
                dispositivo.fabricante = fabricante
            atualizados += 1

    # Quem estava online e não respondeu a este scan passa a offline
    ficaram_offline = 0
    for dispositivo in db.query(Dispositivo).filter(Dispositivo.estado == "online").all():
        if dispositivo.mac not in macs_encontrados:
            dispositivo.estado = "offline"
            ficaram_offline += 1

    db.commit()
    return {
        "encontrados": len(encontrados),
        "novos": novos,
        "atualizados": atualizados,
        "ficaram_offline": ficaram_offline,
        "ignorados_sem_mac": ignorados_sem_mac,
    }
