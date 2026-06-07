# ByteBurguer Cloud Platform

## Visão Geral

A ByteBurguer Cloud Platform é uma arquitetura de microsserviços desenvolvida para suportar operações de restaurantes inteligentes com alto nível de automação. A plataforma integra aplicações web, dispositivos IoT, robôs de cozinha, sistemas de gestão e serviços em nuvem, proporcionando escalabilidade, disponibilidade e segurança.

Este projeto foi desenvolvido como estudo acadêmico para aplicação prática dos conceitos de:

* DevOps
* Segurança da Informação
* Engenharia de Software
* Gestão de Projetos
* Arquitetura e Organização de Computadores
* Computação em Nuvem

---

# Arquitetura da Solução

A plataforma é composta pelos seguintes microsserviços:

| Serviço              | Porta | Função                        |
| -------------------- | ----- | ----------------------------- |
| Auth Service         | 5100  | Autenticação e autorização    |
| Order Service        | 5101  | Gerenciamento de pedidos      |
| Robot Service        | 5102  | Controle dos robôs de cozinha |
| IoT Service          | 5103  | Comunicação com sensores IoT  |
| Franchise Service    | 5104  | Gestão das franquias          |
| Notification Service | 5105  | Envio de notificações         |
| Analytics Service    | 5106  | Métricas e indicadores        |
| User Service         | 5107  | Gestão de usuários            |

---

# Tecnologias Utilizadas

* Docker
* Docker Compose
* GitHub Actions
* Python
* FastAPI
* PostgreSQL
* Redis
* MQTT
* Kubernetes (proposta para produção)
* Prometheus
* Grafana

---

# Configuração do Ambiente

## 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/byteburguer-cloud-platform.git
cd byteburguer-cloud-platform
```

## 2. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
```

Editar o arquivo `.env` conforme necessário.

---

## 3. Executar a Aplicação

Subir todos os serviços:

```bash
make up
```

Verificar logs:

```bash
make logs
```

Parar os serviços:

```bash
make down
```

---

# Endpoints de Saúde

| Serviço      | Endpoint                     |
| ------------ | ---------------------------- |
| Auth         | http://localhost:5100/health |
| Order        | http://localhost:5101/health |
| Robot        | http://localhost:5102/health |
| IoT          | http://localhost:5103/health |
| Franchise    | http://localhost:5104/health |
| Notification | http://localhost:5105/health |
| Analytics    | http://localhost:5106/health |
| User         | http://localhost:5107/health |

---

# Pipeline DevOps

O fluxo DevOps proposto contempla:

1. Desenvolvimento em GitHub.
2. Integração Contínua (CI) com GitHub Actions.
3. Build automatizado de imagens Docker.
4. Testes automatizados.
5. Publicação em Registry Docker.
6. Deploy automatizado em Kubernetes.
7. Monitoramento com Prometheus e Grafana.

---

# Segurança da Informação

A arquitetura contempla:

* Autenticação baseada em JWT.
* Controle de acesso por perfis.
* Criptografia TLS.
* Gestão de segredos.
* Logs centralizados.
* Auditoria de eventos.
* Backup automatizado.
* Monitoramento contínuo.

---

# Escalabilidade

A solução foi projetada para:

* Escalonamento horizontal de microsserviços.
* Balanceamento de carga.
* Alta disponibilidade.
* Tolerância a falhas.
* Recuperação automática de serviços.

---

# Estrutura do Projeto

```text
byteburguer-cloud-platform/
├── auth-service/
├── order-service/
├── robot-service/
├── iot-service/
├── franchise-service/
├── notification-service/
├── analytics-service/
├── user-service/
├── docker-compose.yml
├── Makefile
├── .github/
└── docs/
```

---

# Objetivo Acadêmico

Este projeto demonstra a aplicação integrada dos conceitos de DevOps, Arquitetura de Software, Segurança da Informação e Computação em Nuvem em um ambiente corporativo fictício, simulando uma plataforma moderna para gestão de restaurantes inteligentes.

---

# Autor

**Diego Dos Santos Gonçalves**
Curso Superior de Tecnologia em DevOps
Anhanguera Ampli – 2026

