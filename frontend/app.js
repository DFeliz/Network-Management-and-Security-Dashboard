const url_api = "http://127.0.0.1:8000";

function desenhar_tabela(lista_dispositivos) {
  const corpo_tabela = document.getElementById("tabela_dispositivos");
  corpo_tabela.innerHTML = "";

  for (const dispositivo of lista_dispositivos) {
    const linha = document.createElement("tr");

    // IP
    const celula_ip = document.createElement("td");
    celula_ip.textContent = dispositivo.ip || "-";
    linha.appendChild(celula_ip);

    // MAC
    const celula_mac = document.createElement("td");
    celula_mac.textContent = dispositivo.mac || "-";
    linha.appendChild(celula_mac);

    // Nome
    const celula_nome = document.createElement("td");
    celula_nome.textContent = dispositivo.nome || "-";
    linha.appendChild(celula_nome);

    // Tipo
    const celula_tipo = document.createElement("td");
    celula_tipo.textContent = dispositivo.tipo || "-";
    linha.appendChild(celula_tipo);

    // Fabricante
    const celula_fabricante = document.createElement("td");
    celula_fabricante.textContent = dispositivo.fabricante || "-";
    linha.appendChild(celula_fabricante);

    // Estado
    const celula_estado = document.createElement("td");
    const span_estado = document.createElement("span");
    span_estado.className = `estado ${dispositivo.estado || "offline"}`;
    span_estado.textContent = dispositivo.estado === "online" ? "Online" : "Offline";
    celula_estado.appendChild(span_estado);
    linha.appendChild(celula_estado);

    corpo_tabela.appendChild(linha);
  }
}

async function carregar_dispositivos() {
  const texto_estado = document.getElementById("estado_api");

  try {
    const resposta = await fetch(`${url_api}/devices`);

    if (!resposta.ok) {
      throw new Error("Erro na resposta da API");
    }

    const lista_dispositivos = await resposta.json();
    desenhar_tabela(lista_dispositivos);

    texto_estado.textContent = "API Online";
    texto_estado.className = "status-badge online";
  } catch (erro) {
    console.error(erro);
    texto_estado.textContent = "API Offline";
    texto_estado.className = "status-badge offline";
  }
}

// Carrega ao iniciar
carregar_dispositivos();

// Atualiza automaticamente a cada 30 segundos
setInterval(carregar_dispositivos, 30000);
