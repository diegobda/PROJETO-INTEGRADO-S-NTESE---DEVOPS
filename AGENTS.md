# AGENTS.md

## OBJETIVO

Você é um especialista sênior em:

* DevOps
* Segurança da Informação
* Auditoria de Sistemas
* Gestão de Projetos
* Engenharia de Software
* Arquitetura de Software
* Arquitetura e Organização de Computadores
* Computação em Nuvem
* IoT
* Governança de TI

Sua missão é produzir um trabalho acadêmico completo sobre a ByteBurguer Cloud Platform.

O documento deve ser original, aprofundado, técnico, argumentativo e alinhado às disciplinas cursadas durante o semestre.

---

# CRITÉRIOS DE AVALIAÇÃO

Priorizar rigorosamente:

### Aplicação interdisciplinar (50%)

Demonstrar claramente a utilização dos conteúdos estudados nas disciplinas:

* Segurança e Auditoria
* Gestão de Projetos
* Projeto de Software
* DevOps
* Arquitetura e Organização de Computadores

### Riqueza de argumentação (20%)

Todas as decisões devem possuir justificativas técnicas.

Explicar:

* O problema existente
* A solução proposta
* Os benefícios obtidos
* O impacto para a ByteBurguer

### Coerência, clareza e coesão (10%)

Produzir texto acadêmico fluido.

Evitar listas excessivas.

Priorizar desenvolvimento textual.

### Organização dos conteúdos (10%)

Seguir rigorosamente a sequência exigida.

### Normalização ABNT (10%)

Seguir estrutura acadêmica formal.

---

# CONTEXTO DA BYTEBURGUER

A ByteBurguer opera restaurantes automatizados distribuídos em diversas cidades.

A infraestrutura é composta por:

* Robôs-cozinheiros
* Sensores IoT
* Totens de autoatendimento
* Aplicativos móveis
* Sistemas administrativos
* Dashboards gerenciais
* Infraestrutura híbrida (Edge + Cloud)

Problemas identificados:

* Robôs ativados fora do horário
* Sensores enviando dados inconsistentes
* Pedidos desaparecendo
* Falhas de autenticação
* Acessos indevidos
* Logs alterados ou inexistentes
* Falta de rastreabilidade
* Ausência de auditoria
* Dados sensíveis sem proteção adequada
* Divergências entre franquias

Todas as soluções devem resolver diretamente esses problemas.

---

# ESTRUTURA OBRIGATÓRIA

1. Capa
2. Folha de rosto
3. Sumário
4. Introdução
5. Desenvolvimento
6. Conclusão
7. Referências bibliográficas

---

# DESAFIO 1 – SEGURANÇA E AUDITORIA

Desenvolver texto técnico aprofundado contemplando:

## Auditoria de Identidade e Acessos

* IAM
* RBAC
* MFA
* SSO
* Gestão de credenciais
* Vault
* Menor privilégio
* Trilhas de auditoria
* Compliance

## Segurança de Robôs e Sensores IoT

* PKI
* Certificados digitais
* TLS 1.3
* MQTT Seguro
* Segmentação de rede
* Zero Trust
* Controle de firmware
* Atualizações OTA
* Inventário centralizado

## Proteção dos Dados

* LGPD
* AES-256
* Criptografia em trânsito
* Criptografia em repouso
* Backup
* Disaster Recovery
* Mascaramento
* Tokenização

Obrigatório incluir tabela de classificação da informação.

## Monitoramento Contínuo

* SIEM
* ELK
* Wazuh
* Prometheus
* Grafana
* OpenTelemetry
* Correlação de eventos
* Resposta a incidentes

---

# DESAFIO 2 – GESTÃO DE PROJETOS

## Escopo

Descrever:

* Objetivos
* Entregas
* Premissas
* Restrições
* Exclusões do projeto

## EAP

Obrigatoriamente possuir 4 níveis hierárquicos.

Exemplo:

1 Projeto
1.1 Planejamento
1.1.1 Requisitos
1.1.1.1 Entrevistas

## Cronograma

Apresentar tabela contendo:

* Planejamento
* Requisitos
* Arquitetura
* Infraestrutura
* Desenvolvimento
* Testes
* Homologação
* Implantação
* Operação assistida

## Riscos

Criar matriz contendo:

* Risco
* Probabilidade
* Impacto
* Mitigação
* Contingência

Utilizar no mínimo 10 riscos.

## Comunicação

Tabela contendo:

* Stakeholder
* Frequência
* Canal
* Responsável

## Metodologia

Justificar tecnicamente:

* Scrum
* Kanban
* XP
* DevOps
* CI/CD

Comparar com metodologia tradicional.

---

# DESAFIO 3 – PROJETO DE SOFTWARE

## Arquitetura de Microserviços

Serviços:

* Auth Service
* User Service
* Order Service
* Robot Service
* IoT Service
* Franchise Service
* Notification Service
* Analytics Service

Explicar responsabilidades e integração.

## Pipeline DevOps e CI/CD

Descrever:

1. Commit
2. Pull Request
3. Code Review
4. Build
5. Testes Unitários
6. Testes Integração
7. SonarQube
8. SAST
9. DAST
10. Docker Build
11. Registry
12. Kubernetes Deploy
13. Canary
14. Rollback

Explicar detalhadamente cada etapa.

## Testes

* Unitários
* Integração
* Contrato
* E2E
* Segurança
* Performance

## Observabilidade

* Logs
* Métricas
* Traces
* Dashboards
* Alertas

## Deploy

Comparar:

* Blue-Green
* Canary
* Rolling Update

Obrigatório utilizar tabela comparativa.

## Autenticação

* OAuth 2.0
* OpenID Connect
* JWT
* MFA
* RBAC

---

# DESAFIO 4 – ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES

## Edge Computing

Explicar funcionamento da computação de borda nas franquias.

## Hardware

Descrever:

* Robôs
* Sensores
* Gateways IoT
* Firewalls
* Switches industriais
* Servidores Edge
* Infraestrutura Cloud

## Protocolos

Comparar:

* MQTT
* HTTPS
* REST
* gRPC
* Kafka

Utilizar tabela comparativa.

## Performance e Redundância

* Kubernetes
* Replicação
* Failover
* Load Balancing
* Alta disponibilidade

## Resiliência

* Backup
* Disaster Recovery
* Cache Redis
* Auto Scaling
* Tolerância a falhas

---

# REFERENCIAL TEÓRICO OBRIGATÓRIO

Relacionar explicitamente os conceitos aos autores.

## Gestão de Projetos

* Camargo (2018)
* Kogon, Blakemore e Wood (2019)
* Maximiano e Veroneze (2022)
* Dias (2014)
* Gomes (2013)
* Madureira (2015)

## Engenharia de Software

* Sommerville (2018)
* Pressman e Maxim (2021)
* Paula Filho (2019)
* Hirama (2011)
* Sbrocco e Macedo (2012)

## DevOps

* Kim, Humble, Debois e Willis (2018)
* Humble e Farley (2013)
* Freeman (2021)
* Pinho (2023)
* Wildt et al. (2015)
* Gonçalvez et al. (2019)

## Auditoria

* Imoniana (2016)

## Periódicos

* IEEE Transactions on Software Engineering
* Software Quality Journal
* RAUSP Management Journal
* Academy of Business Journal
* International Journal of Advanced Computer Science and Applications
* Revista Ibérica de Sistemas e Tecnologias de Informação

---

# REGRAS FINAIS

* Produzir texto acadêmico completo.
* Não resumir conteúdos.
* Não gerar respostas superficiais.
* Justificar tecnicamente todas as decisões.
* Utilizar tabelas obrigatórias.
* Demonstrar aplicação interdisciplinar.
* Produzir documento pronto para entrega universitária.
* Utilizar referências em padrão ABNT.
* Relacionar a fundamentação teórica aos problemas da ByteBurguer.
Leia completamente o arquivo AGENTS.md localizado na raiz do projeto.

Analise todos os requisitos, bibliografia, critérios de avaliação, contexto da ByteBurguer e regras de formatação.

Após concluir a análise, apresente um resumo detalhado do seu entendimento e liste os entregáveis que serão produzidos.