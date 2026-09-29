# Network Management and Security Dashboard
# Network Management and Security Dashboard

## Sobre o Projeto

O **Network Management and Security Dashboard** é uma aplicação desenvolvida para permitir a **monitorização, gestão e proteção centralizada de uma rede** através de uma interface simples e intuitiva.

O objetivo é permitir que um administrador consiga visualizar os dispositivos ligados à rede, acompanhar a utilização da rede, identificar comportamentos suspeitos e aplicar regras de segurança sem ter de utilizar várias ferramentas diferentes.

O sistema pretende ser adequado principalmente para **redes domésticas, pequenas empresas e ambientes escolares**, onde seja necessário ter maior controlo sobre os dispositivos e sobre o tráfego da rede.

O projeto encontra-se em desenvolvimento.

---

## Objetivos

Os principais objetivos do projeto são:

* Identificar automaticamente os dispositivos ligados à rede.
* Apresentar informações como endereço IP, endereço MAC e tipo de dispositivo.
* Monitorizar o tráfego da rede.
* Permitir ao administrador consultar informações sobre a utilização da rede.
* Detetar dispositivos desconhecidos ou não autorizados.
* Permitir bloquear ou isolar dispositivos.
* Criar regras de acesso à rede.
* Permitir bloquear determinados domínios ou sites.
* Registar acontecimentos e ações realizadas pelo administrador.
* Detetar comportamentos potencialmente maliciosos.
* Proteger a rede contra tentativas de exploração e reconhecimento.
* Impedir que a rede seja utilizada como servidor, relay ou **exit node de uma VPN**.
* Manter permitido o uso normal de VPN por utilizadores da rede.

### Regra relativamente às VPN

O projeto **não pretende impedir os utilizadores de utilizarem VPN**.

Por exemplo, um computador dentro da rede pode ligar-se a um servidor VPN externo.

O que o sistema pretende impedir é que um dispositivo utilize a ligação à Internet da rede para funcionar como:

* servidor VPN;
* exit node;
* relay;
* proxy para terceiros;
* ponto de acesso através do qual outras pessoas utilizem a rede.

Desta forma, o objetivo é proteger a rede contra utilização abusiva sem impedir a utilização legítima de VPN.

---

## Funcionalidades

### 1. Identificação de dispositivos

O sistema deverá realizar uma descoberta automática dos dispositivos presentes na rede.

Para cada dispositivo poderão ser apresentados dados como:

* IP;
* MAC;
* fabricante;
* nome do dispositivo, quando disponível;
* tipo de dispositivo;
* estado online/offline.

Exemplos de dispositivos:

* Computadores;
* Telemóveis;
* Tablets;
* Smart TVs;
* Consolas;
* Impressoras;
* Dispositivos IoT.

---

### 2. Monitorização da rede

O dashboard deverá apresentar informação sobre a utilização da rede em tempo real.

Entre os dados previstos encontram-se:

* tráfego de entrada e saída;
* quantidade de dados transferidos;
* dispositivos com maior utilização;
* protocolos utilizados;
* ligações estabelecidas;
* domínios contactados, quando tecnicamente possível.

---

### 3. Histórico

O sistema deverá guardar informação relevante para permitir consultar acontecimentos anteriores.

Será possível, por exemplo, consultar:

* dispositivos que estiveram ligados;
* atividade registada;
* alertas de segurança;
* alterações realizadas pelo administrador;
* bloqueios realizados;
* acontecimentos suspeitos.

---

### 4. Controlo dos dispositivos

O administrador poderá aplicar ações de segurança diretamente através do dashboard.

Entre as funcionalidades previstas:

* Bloquear um dispositivo;
* Retirar um dispositivo da rede;
* Isolar um dispositivo;
* Criar uma lista de dispositivos autorizados;
* Criar uma lista de dispositivos bloqueados;
* Aplicar regras específicas a determinados dispositivos.

---

### 5. Filtro de acesso

O sistema deverá permitir criar regras para controlar o acesso a determinados domínios ou serviços.

Poderá ser possível:

* bloquear um domínio;
* bloquear categorias de conteúdos;
* aplicar regras a toda a rede;
* aplicar regras apenas a determinados dispositivos.

---

### 6. Deteção de ameaças

Uma das partes principais do projeto será a segurança da rede.

O sistema deverá procurar identificar situações como:

* dispositivos desconhecidos;
* port scanning;
* comportamento anómalo;
* tentativas de acesso não autorizado;
* ligações para endereços suspeitos;
* possíveis comunicações com servidores maliciosos;
* alterações suspeitas de endereço MAC.

Quando for detetada uma situação suspeita, o dashboard poderá apresentar um alerta ao administrador.

---

### 7. Proteção contra utilização abusiva da rede

O sistema deverá verificar se algum dispositivo está a tentar utilizar a rede de forma abusiva.

Um dos casos específicos será a tentativa de transformar um dispositivo da rede num servidor ou **exit node de VPN**.

O sistema deverá procurar identificar:

* servidores VPN expostos;
* portas associadas a serviços VPN;
* comportamentos compatíveis com relay ou exit node;
* utilização anormal do tráfego.

Quando possível, o administrador poderá bloquear ou isolar o dispositivo.

---

# Tecnologias e Linguagens

## Linguagens de programação

### Python

Será utilizada principalmente no **backend**.

Python será responsável pela lógica da aplicação, comunicação com as ferramentas de rede, processamento de informação e disponibilização da API.

### HTML

Será utilizada para estruturar as páginas da interface.

### CSS

Será utilizada para definir o aspeto visual da aplicação.

### JavaScript

Será utilizada para criar funcionalidades interativas no dashboard e atualizar informações apresentadas ao utilizador.

### SQL

Será utilizada para trabalhar com a base de dados e guardar informações do sistema.

---

# Ferramentas e Aplicações

| Ferramenta                  | Utilização                                            |
| --------------------------- | ----------------------------------------------------- |
| **Visual Studio Code**      | Desenvolvimento do projeto                            |
| **Python**                  | Desenvolvimento do backend                            |
| **FastAPI**                 | Criação da API                                        |
| **HTML / CSS / JavaScript** | Desenvolvimento da interface                          |
| **PostgreSQL**              | Base de dados                                         |
| **Docker**                  | Execução e isolamento dos serviços                    |
| **Git**                     | Controlo de versões                                   |
| **GitHub**                  | Armazenamento e colaboração no projeto                |
| **Nmap**                    | Descoberta e análise de dispositivos e serviços       |
| **Suricata**                | Deteção de tráfego suspeito e ameaças                 |
| **Wireshark**               | Análise de tráfego durante o desenvolvimento e testes |
| **tcpdump**                 | Captura de tráfego de rede                            |
| **nftables / firewall**     | Aplicação de regras de bloqueio e controlo            |
| **Redis**                   | Dados temporários e informação em tempo real          |

Algumas destas ferramentas poderão ser adicionadas numa fase posterior do desenvolvimento.

---

# Arquitetura do Projeto

O projeto será dividido em diferentes componentes.

```text
                    REDE
                      │
                      ▼
             ┌─────────────────┐
             │ Ferramentas de  │
             │ monitorização   │
             │ Nmap / Suricata │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │     Backend     │
             │ Python / FastAPI│
             └────────┬────────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
      ┌─────────────┐   ┌─────────────┐
      │ PostgreSQL  │   │    Redis    │
      │  Base dados │   │ Tempo real  │
      └─────────────┘   └─────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    Dashboard    │
             │  Web Interface  │
             └─────────────────┘
                      │
                      ▼
               ADMINISTRADOR
```

---

# O que o projeto pode melhorar face ao que já existe

Existem várias ferramentas de administração e segurança de redes, mas muitas delas têm funções específicas ou exigem conhecimentos técnicos para serem configuradas.

Este projeto pretende juntar várias dessas funções numa única interface.

### 1. Centralização

Em vez de utilizar várias ferramentas separadamente, o administrador poderá consultar diferentes informações através de um único dashboard.

### 2. Interface simples

O projeto pretende apresentar informações técnicas de forma mais simples e compreensível, permitindo que um utilizador consiga perceber rapidamente o estado da rede.

### 3. Segurança integrada

A monitorização e a segurança estarão integradas na mesma aplicação.

O administrador poderá identificar um problema e, a partir do próprio dashboard, aplicar uma ação de segurança.

### 4. Proteção específica contra abuso da rede

Uma característica importante do projeto será a preocupação com a utilização da rede como servidor ou exit node de VPN.

O objetivo não é bloquear VPNs utilizadas normalmente pelos utilizadores, mas identificar situações em que um dispositivo esteja a utilizar a rede para fornecer uma VPN ou relay a terceiros.

### 5. Visibilidade da rede

O administrador terá uma visão centralizada dos dispositivos existentes e dos acontecimentos relevantes da rede.

### 6. Automatização

Sempre que possível, tarefas que normalmente teriam de ser realizadas manualmente poderão ser automatizadas, como:

* descoberta de dispositivos;
* geração de alertas;
* identificação de comportamentos suspeitos;
* aplicação de determinadas regras;
* registo de acontecimentos.

---

# Segurança

A segurança será uma parte fundamental do projeto.

O sistema deverá utilizar diferentes mecanismos para tentar proteger a rede contra:

* dispositivos não autorizados;
* reconhecimento da rede;
* port scanning;
* serviços expostos;
* comportamentos anómalos;
* comunicações suspeitas;
* utilização abusiva da ligação;
* servidores VPN não autorizados;
* utilização da rede como relay ou exit node.

As ações de bloqueio deverão ser realizadas através das ferramentas de firewall e dos mecanismos de controlo disponíveis no sistema.

---

# Estado Atual

O projeto encontra-se atualmente em desenvolvimento.

### Planeado

* [x] Criação do repositório
* [x] Estrutura inicial do projeto
* [ ] Desenvolvimento do backend
* [ ] Desenvolvimento da API
* [ ] Desenvolvimento do dashboard
* [ ] Descoberta de dispositivos
* [ ] Base de dados
* [ ] Monitorização de tráfego
* [ ] Sistema de alertas
* [ ] Controlo de dispositivos
* [ ] Regras de firewall
* [ ] Deteção de comportamentos suspeitos
* [ ] Proteção contra utilização da rede como VPN
* [ ] Testes de segurança
* [ ] Documentação final

---

# Objetivo Final

O objetivo final é desenvolver uma plataforma que permita ao administrador **ver, compreender e proteger a sua rede a partir de um único local**.

O sistema deverá combinar monitorização, gestão e segurança numa interface simples, permitindo identificar problemas rapidamente e aplicar medidas de proteção sem ser necessário utilizar várias aplicações diferentes.

---

## Autor

**DFeliz**

Projeto desenvolvido no âmbito da formação em **Programação de Sistemas Informáticos**.

---

## Licença

Este projeto encontra-se atualmente em desenvolvimento.
