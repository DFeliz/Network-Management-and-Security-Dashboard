// Dados de exemplo.
const dispositivos = [
  { id: 1, ip: "192.168.1.10", nome: "PC", tipo: "PC", online: true, bloqueado: false },
  { id: 2, ip: "192.168.1.11", nome: "Telemóvel", tipo: "Telemóvel", online: true, bloqueado: false },
  { id: 3, ip: "192.168.1.12", nome: "Smart TV", tipo: "Smart TV", online: false, bloqueado: false },
];

function estado_de(dispositivo) {
  if (dispositivo.bloqueado) return { classe: "bloqueado", texto: "Bloqueado" };
  if (dispositivo.online) return { classe: "online", texto: "Online" };
  return { classe: "offline", texto: "Offline" };
}

function desenhar_tabela() {
  const corpo_tabela = document.getElementById("tabela-dispositivos");
  corpo_tabela.innerHTML = "";

  dispositivos.forEach((dispositivo) => {
    const estado = estado_de(dispositivo);
    const linha = document.createElement("tr");
    linha.innerHTML = `
      <td>${dispositivo.nome}</td>
      <td>${dispositivo.ip}</td>
      <td>${dispositivo.tipo}</td>
      <td><span class="estado ${estado.classe}">${estado.texto}</span></td>
      <td><button data-id="${dispositivo.id}">${dispositivo.bloqueado ? "Desbloquear" : "Bloquear"}</button></td>
    `;
    corpo_tabela.appendChild(linha);
  });

  const total_online = dispositivos.filter((d) => d.online && !d.bloqueado).length;
  document.getElementById("resumo").textContent =
    `${dispositivos.length} dispositivos · ${total_online} online`;
}

// Clicar num botão bloqueia/desbloqueia o dispositivo
document.getElementById("tabela-dispositivos").addEventListener("click", (evento) => {
  const botao = evento.target.closest("button");
  if (!botao) return;

  const dispositivo = dispositivos.find((d) => d.id === Number(botao.dataset.id));
  dispositivo.bloqueado = !dispositivo.bloqueado;
  desenhar_tabela();
});

desenhar_tabela();