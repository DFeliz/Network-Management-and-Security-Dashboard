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

function mostrar_mensagem_scan(texto, tipo) {
  const mensagem_scan = document.getElementById("mensagem_scan");
  mensagem_scan.textContent = texto;
  mensagem_scan.className = tipo ? `mensagem-scan ${tipo}` : "mensagem-scan";
}

async function fazer_scan() {
  const botao_scan = document.getElementById("botao_scan");

  // Desativa o botão para não lançar dois scans ao mesmo tempo
  botao_scan.disabled = true;
  botao_scan.textContent = "A analisar a rede...";
  mostrar_mensagem_scan("A analisar a rede, isto pode demorar um pouco.", "");

  try {
    const resposta = await fetch(`${url_api}/devices/scan`, { method: "POST" });
    const dados = await resposta.json().catch(() => ({}));

    if (!resposta.ok) {
      // A API explica o problema em "detail" (ex.: falta o REDE_ALVO no .env)
      const motivo = typeof dados.detail === "string" ? dados.detail : "Erro ao fazer o scan.";
      throw new Error(motivo);
    }

    let resumo = `Rede ${dados.rede} · Encontrados: ${dados.encontrados}`
      + ` · Novos: ${dados.novos}`
      + ` · Atualizados: ${dados.atualizados}`
      + ` · Ficaram offline: ${dados.ficaram_offline}`;
    if (dados.ignorados_sem_mac > 0) {
      resumo += ` · Sem MAC (ignorados): ${dados.ignorados_sem_mac}`;
    }
    mostrar_mensagem_scan(resumo, "sucesso");

    await carregar_dispositivos();
  } catch (erro) {
    console.error(erro);
    // Um TypeError do fetch quer dizer que nem chegou à API (desligada ou bloqueada)
    const texto_erro = erro instanceof TypeError
      ? "Não foi possível ligar à API. Confirma que o uvicorn está a correr."
      : erro.message;
    mostrar_mensagem_scan(texto_erro, "erro");
  } finally {
    botao_scan.disabled = false;
    botao_scan.textContent = "Scan agora";
  }
}

// Carrega ao iniciar
carregar_dispositivos();

// Atualiza automaticamente a cada 30 segundos
setInterval(carregar_dispositivos, 30000);
