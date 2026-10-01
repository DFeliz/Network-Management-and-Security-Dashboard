const url_api = "http://127.0.0.1:8000";

function desenhar_tabela(lista_dispositivos) {
  const corpo_tabela = document.getElementById("tabela_dispositivos");
  corpo_tabela.innerHTML = "";

  for (const dispositivo of lista_dispositivos) {
    const linha = document.createElement("tr");

    for (const campo of ["ip", "mac", "tipo", "estado"]) {
      const celula = document.createElement("td");
      celula.textContent = dispositivo[campo];
      linha.appendChild(celula);
    }

    corpo_tabela.appendChild(linha);
  }
}

async function carregar_dispositivos() {
  const texto_estado = document.getElementById("estado_api");

  try {
    const resposta = await fetch(`${url_api}/devices`);
    const lista_dispositivos = await resposta.json();
    desenhar_tabela(lista_dispositivos);
    texto_estado.textContent = "API online";
  } catch (erro) {
    texto_estado.textContent = "Não foi possível ligar à API";
  }
}

carregar_dispositivos();