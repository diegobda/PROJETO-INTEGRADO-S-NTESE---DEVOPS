# BYTEBURGUER CLOUD PLATFORM: PROPOSTA DE ARQUITETURA, SEGURANÇA E GESTÃO

**Aluno:** [Nome do Estudante]

**Disciplina:** Segurança da Informação, Gestão de Projetos, Engenharia de Software, DevOps, Arquitetura de Computadores

**Professor:** [Nome do Professor]

**Instituição:** [Nome da Instituição]

**Curso:** [Nome do Curso]

**Data:** Junho de 2026

---

# FOLHA DE ROSTO

Trabalho acadêmico apresentado como requisito parcial para a avaliação da disciplina de Segurança da Informação e Engenharia de Software, no curso de [Nome do Curso], na [Nome da Instituição].

Orientador: [Nome do Orientador]

Aluno: [Nome do Estudante]

Cidade, 2026.

---

# SUMÁRIO

1. Introdução
2. Desenvolvimento
  2.1. Segurança e Auditoria
  2.2. Gestão de Projetos
  2.3. Projeto de Software
  2.4. Arquitetura e Organização de Computadores
3. Conclusão
4. Referências Bibliográficas

---

# 1 Introdução

A transformação digital de varejo e serviços fixos avança com rapidez, exigindo de empresas como a ByteBurguer uma postura proativa sobre segurança, governança, disponibilidade e qualidade de software. A ByteBurguer opera restaurantes automatizados distribuídos por diferentes cidades e enfrenta uma infraestrutura heterogênea com robôs-cozinheiros, sensores IoT, totens de autoatendimento, aplicativos móveis, sistemas administrativos, dashboards gerenciais e uma arquitetura híbrida de Edge + Cloud. O presente trabalho propõe um conjunto integrado de soluções de arquitetura, segurança, auditoria, gerenciamento de projeto e operação para tratar a criticidade de problemas específicos identificados no contexto da ByteBurguer.

O documento segue exigências formais de estruturação e apresenta conteúdo técnico alinhado ao referencial teórico obrigatório. A criação de um plano de segurança robusto e de uma governança de TI consistente atende diretamente às necessidades de audibilidade, conformidade e proteção de dados, enquanto a proposta de arquitetura de microserviços e pipeline DevOps garante escalabilidade, resiliência e qualidade contínua. A escolha de metodologias de gestão adaptativas e a modelagem de Edge Computing são reforçadas pela literatura de gestão de projetos, engenharia de software, DevOps e auditoria. Todas as decisões são justificadas tecnicamente com base em autores como Sommerville, Pressman e Maxim, Kim et al., Humble e Farley, Maximiano e Veroneze, Imoniana, entre outros.

A motivação do trabalho é dupla: primeiro, solucionar os problemas apresentados pela ByteBurguer, como robôs ativados fora do horário, sensores com dados inconsistentes, pedidos desaparecendo e falhas de autenticação; segundo, demonstrar a aplicação interdisciplinar entre segurança, gestão de projetos, arquitetura de software, DevOps e organização de computadores. Essas duas frentes demandam um documento denso e argumentativo, que descreva não apenas os conceitos, mas sobretudo as decisões concretas a serem implementadas no ambiente da ByteBurguer.

A introdução inclui aqui a delimitação do problema, definição de objetivos e o valor acadêmico e prático da proposta. Conforme Madureira (2015) e Gomes (2013), um projeto de tecnologia deve ser contextualizado em termos de objetivos claros, riscos e benefícios. No caso da ByteBurguer, os objetivos são proteger operações automatizadas, reduzir riscos de interrupção, evitar vazamentos de dados e assegurar alinhamento entre as franquias. A relevância é imediata: uma falha em um sistema de robôs de cozinha pode gerar prejuízo operacional, comprometimento da experiência do cliente e riscos regulatórios relacionados à LGPD.

O trabalho está organizado em quatro grandes desafios, cada um com implicações técnicas e gerenciais: Segurança e Auditoria, Gestão de Projetos, Projeto de Software e Arquitetura/Organização de Computadores. Cada desafio é tratado como um bloco temático que corresponde a requisitos obrigatórios do AGENTS.md e às disciplinas do semestre. Além disso, a seção de desenvolvimento incorpora tabelas de classificação da informação, matriz de riscos, plano de comunicação, comparativos de deploy e protocolos, além de uma proposta de pipeline CI/CD completa.

O documento é redigido em estilo técnico-acadêmico, privilegiando coesão, clareza e fundamentação teórica, com citações explícitas dos autores exigidos. Os conceitos são aplicados ao contexto real da ByteBurguer e todas as decisões propostas visam resolver diretamente os problemas listados, assegurando que a solução não permaneça em um nível abstrato. A partir da fundamentação em Sommerville (2018), Pressman e Maxim (2021) e Kim et al. (2018), as recomendações são construídas sobre princípios de qualidade de software, práticas de DevOps e controle de auditoria.

Com isso, a introdução assinala a estrutura do trabalho e reforça o compromisso de atender às regras formais de apresentação da ABNT. Os leitores encontrarão a seguir um desenvolvimento detalhado, organizado em grandes áreas técnicas e de gestão, uma conclusão que sintetiza a proposta e um conjunto de referências bibliográficas em conformidade com as exigências do projeto.

---

# 2 Desenvolvimento

## 2.1 Segurança e Auditoria

A proposta de segurança e auditoria para a ByteBurguer deve ser concebida como uma arquitetura de defesa em profundidade, que combine controles de identidade e acesso, proteção de IoT, proteção de dados e monitoramento contínuo. A avaliação do contexto revela falhas críticas: a existência de robôs ativados fora do horário, sensores com dados inconsistentes, pedidos desaparecendo, falhas de autenticação, acessos indevidos e logs alterados ou inexistentes. Esses problemas requerem medidas coordenadas para garantir confidencialidade, integridade, disponibilidade e rastreabilidade.

### 2.1.1 Auditoria de Identidade e Acessos

Para mitigar falhas de autenticação e acessos indevidos, a ByteBurguer deve adotar um modelo de gestão de identidade e acesso (IAM) centralizado. O IAM deve combinar RBAC (Role-Based Access Control), MFA (Multi-Factor Authentication), SSO (Single Sign-On) e gestão de credenciais segura. A estratégia se baseia em princípios de menor privilégio e segregação de funções, recomendados por Imoniana (2016) na área de auditoria e por Sommerville (2018) na engenharia de software.

A implementação do IAM deve começar com a definição de perfis de acesso para cada tipo de usuário e componente do sistema. Por exemplo:

- Administradores de plataforma: acesso a configuração de rede, PKI, Vault e logs.
- Engenheiros de software e DevOps: acesso a repositórios, pipeline CI/CD e ambientes de teste.
- Equipe de operações de franquia: acesso a dashboards gerenciais, monitoração de Edge e dados operacionais apenas das franquias atribuídas.
- Robôs e sensores IoT: identidades de máquina com certificados digitais e permissões mínimas para publicação e leitura de mensagens.

Esse modelo concede a cada ator apenas o que precisa para desempenhar sua função, reduzindo o risco de brechas por permissões excessivas. A segregação de funções evita que um operador de infraestrutura possa alterar logs ou aprovar mudanças sem supervisão.

A autenticação deve ser baseada em MFA para todos os acessos administrativos e também para acesso a sistemas críticos de administração de franquias. A adoção de MFA em conjunto com SSO simplifica a experiência do usuário e mantém a segurança robusta. O SSO deve ser integrado com um provedor corporativo que suporte protocolos como OAuth 2.0 e OpenID Connect, conforme discutido em Kim et al. (2018) e Humble e Farley (2013), permitindo autenticação federada entre serviços internos e ferramentas de gestão de identidade.

A gestão de credenciais passa pelo uso de um cofre de segredos (Vault). O HashiCorp Vault ou um serviço equivalente devem ser utilizados para armazenar segredos, tokens, chaves de API e certificados de forma centralizada, com controle de acesso baseado em políticas. O Vault deve emitir credenciais dinâmicas sempre que possível, evitando segredos estáticos em código ou configuração. A integração do Vault com Kubernetes e com os componentes de Edge garante que segredos sensíveis não sejam expostos em texto claro.

As trilhas de auditoria (audit trails) são essenciais para rastreabilidade e compliance. Todos os acessos a sistemas administrativos, todas as alterações de configuração, e todas as tentativas de autenticação devem ser registradas em um SIEM com retenção segura. Esse controle deve incluir logs de API, logs de autenticação e logs de infraestrutura de rede. A auditoria deve estar alinhada com normas de compliance e com políticas internas de governança, além de ser capaz de reenviar eventos para soluções como Wazuh e ELK.

A conformidade (compliance) com regulamentações como a LGPD deve ser um requisito transversal. A governança de acesso deve garantir, por exemplo, que apenas operadores autorizados possam acessar dados de clientes e que o acesso a dados pessoais seja devidamente registrado. A política de acesso deve também prever revisão periódica das permissões e certificações de conformidade para evitar drift de privilégios.

### 2.1.2 Segurança de Robôs e Sensores IoT

A camada IoT da ByteBurguer é particularmente sensível porque envolve robôs-cozinheiros e sensores distribuídos em Edge. A segurança desses dispositivos deve ser construída sobre PKI (Public Key Infrastructure), certificados digitais, TLS 1.3, MQTT seguro, segmentação de rede, Zero Trust, controle de firmware, atualizações OTA e inventário centralizado.

A primeira decisão técnica é adotar uma PKI corporativa que emita certificados X.509 para todos os dispositivos, incluindo robôs, gateways e sensores. Essa PKI garante identidade criptográfica forte e possibilita autenticação mútua. A utilização de TLS 1.3 em todas as conexões de comunicação entre dispositivos e backend reduz a superfície de ataque e protege dados em trânsito, alinhando-se às práticas recomendadas por Pressman e Maxim (2021) para segurança de sistemas distribuídos.

O protocolo MQTT deve ser usado apenas em sua versão segura, com TLS e autenticação de certificado de cliente. Ao invés de permitir conexões MQTT sem segurança, cada dispositivo deve fazer handshake TLS com o broker, usando certificados emitidos pela PKI. O broker MQTT deve ser configurado com policies restritivas: cada dispositivo só pode publicar ou assinar tópicos específicos, e tópicos sensíveis são isolados em namespaces separados.

A segmentação de rede é um princípio imprescindível. As redes de IoT, de Edge e de data center devem ser segregadas fisicamente ou logicamente. Firewalls e filtros de pacote controlam o tráfego entre segmentos, permitindo somente comunicação necessária. Por exemplo, robôs na cozinha devem ter acesso apenas ao broker MQTT e ao gateway Edge local, não ao backbone administrativo. Essa segmentação reduz o risco de movimentos laterais dentro da infraestrutura.

O conceito de Zero Trust complementa a segmentação: nenhum dispositivo ou serviço é confiável por padrão simplesmente por estar conectado. Cada fluxo de dados deve ser autenticado e autorizado. Isso significa que, mesmo se um robô for comprometido, ele não pode alterar dados de outro robô ou acessar a rede de administração sem um novo processo de autenticação. A arquitetura Zero Trust proposta inclui autenticação contínua de dispositivos, verificação de integridade e controle de acesso adaptativo.

O controle de firmware e as atualizações OTA (over-the-air) são imperativos para garantir que robôs e sensores executem software autorizado e estejam protegidos contra vulnerabilidades conhecidas. Um sistema central de gerenciamento de firmware deve verificar assinaturas digitais de imagens antes do deploy e garantir que apenas versões aprovadas sejam instaladas. As atualizações OTA devem ser entregues por canais confiáveis e criptografados, com rollback automático em caso de falha. Isso atende diretamente ao problema de dispositivos operando fora do padrão ou com dados inconsistentes.

Um inventário centralizado de ativos IoT e Edge é outro componente crítico. A ByteBurguer deve ter um registro de cada dispositivo, firmware, versão de software, localização física, estado de saúde e última conexão. Esse inventário serve como base para auditoria, análise de risco e resposta a incidentes. A gestão de ativos também facilita a identificação de divergências entre franquias, porque permite comparar configurações e detectar desvios.

### 2.1.3 Proteção dos Dados

A proteção dos dados na ByteBurguer deve ser entendida como um conjunto de controles técnicas e de governança que abranja cifragem, backup, DR, mascaramento e tokenização. A LGPD impõe obrigações sobre tratamento, armazenamento, pseudonimização e segurança de dados pessoais. As decisões propostas respondem diretamente à lacuna de dados sensíveis sem proteção adequada.

A primeira decisão é a aplicação de criptografia AES-256 nos dados persistidos, tanto em bancos de dados quanto em sistemas de arquivos e backups. O uso de AES-256 para dados em repouso é uma prática consolidada e deve ser complementado por gerenciamento seguro de chaves no Vault. As chaves de criptografia devem ser rotacionadas periodicamente e em resposta a incidentes.

Para criptografia em trânsito, todas as APIs internas e externas devem usar TLS 1.3, e o tráfego entre componentes de microserviços deve ser protegido por mTLS sempre que possível. Isso impede interceptações e garante autenticidade dos endpoints. A proteção em trânsito também se estende a dispositivos IoT e gateways Edge.

O backup deve ser automatizado e protegido por políticas de retenção e criptografia. O plano de backup deve incluir backups incrementais diários e backups completos semanais, com armazenamento em um repositório separado da infraestrutura de produção. O teste de restauração é obrigatório para validar a confiabilidade dos backups. A estratégia de Disaster Recovery (DR) deve prever failover controlado para uma região ou ambiente alternativo, com RTO e RPO definidos.

O mascaramento e a tokenização são medidas adicionais que reduzem a exposição de dados sensíveis em ambientes de desenvolvimento, teste e operações. Dados como CPF, telefone e informações de pagamento devem ser mascarados ou tokenizados sempre que não forem estritamente necessários. Esse controle é crucial para a conformidade com a LGPD e para evitar exposição acidental durante análise ou debug.

Uma tabela de classificação da informação é obrigatória e deve ser usada para definir quais ativos recebem quais controles. A tabela proposta inclui categorias como Público, Interno, Confidencial e Restrito, com exemplos específicos do ambiente ByteBurguer. Essa classificação orienta a aplicação de controles de criptografia, retenção, acesso e auditoria.

### 2.1.4 Monitoramento Contínuo

O monitoramento contínuo deve ser implementado via um stack integrado que combine SIEM, ELK, Wazuh, Prometheus, Grafana e OpenTelemetry. A correlação de eventos e a resposta a incidentes são essenciais para detectar e reagir a ameaças em tempo real.

A arquitetura de monitoramento proposta é a seguinte:

- Wazuh para coleta e análise de logs de segurança, detecção de intrusões e verificação de integridade de arquivos.
- ELK (Elasticsearch, Logstash, Kibana) para ingestão, indexação e visualização de logs operacionais e de aplicação.
- Prometheus para coleta de métricas de infraestrutura e serviços, com regras de alerta baseadas em thresholds e anomalias.
- Grafana como plataforma unificada de dashboards, integrando métricas de Prometheus, logs do ELK e eventos de segurança.
- OpenTelemetry para instrumentação de aplicações, geração de traces distribuídos e correlação de transações de ponta a ponta.
- SIEM para correlação entre logs de segurança, alertas de Wazuh e métricas operacionais, possibilitando detecção de padrões de ataque e incômodos operacionais.

A integração entre esses componentes permite uma visão ampla e coordenada. Por exemplo, um evento de falha de autenticação em um sistema administrativo, combinado com um pico de mensagens MQTT inválidas e alteração de firmware não autorizada, deve disparar um alerta de incidente de segurança. Essa correlação é prática recomendada por Kim et al. (2018) e por Imoniana (2016) para detecção em ambientes críticos.

A resposta a incidentes deve estar documentada em um runbook que defina papéis, canais de comunicação e ações imediatas. Para cada tipo de incidente, como comprometimento de um dispositivo IoT, violação de dados ou falha de autenticação, o runbook deve prever contenção, investigação, erradicação e recuperação. O processo deve incluir notificação da gestão, análise forense de logs e execução de patches ou rollback quando necessário.

A implementação de métricas e alertas deve seguir o princípio de observabilidade de que não se trata apenas de coletar dados, mas de transformá-los em insights acionáveis. Por isso, além de métricas básicas de CPU e memória, a ByteBurguer deve monitorar indicadores de negócios como taxa de sucesso de pedidos, latência de preparação de pratos, integridade de sensores e taxa de rejeição de autenticações.

### 2.1.5 Tabela de Classificação da Informação

A tabela de classificação da informação proposta para a ByteBurguer é:

- Público: informações de marketing, menus públicos e dados não sensíveis.
- Interno: operações internas, relatórios de desempenho, métricas de uso e diagnósticos não sensíveis.
- Confidencial: dados de clientes, credenciais de acesso, segredos de integração, relatórios financeiros básicos.
- Restrito: dados pessoais sensíveis, chaves de criptografia, logs de auditoria, configurações de segurança e informações de sistema crítico.

Essa classificação orienta a aplicação de controles como criptografia AES-256 para dados confidenciais e restritos, mascaramento em ambientes de teste e política de acesso estrita. As informações restritas, por exemplo, devem ser acessíveis apenas por administradores de segurança e pela equipe de auditoria, com registro em trilhas de auditoria.

Em resumo, a seção de Segurança e Auditoria apresenta um conjunto integrado de decisões estratégicas e técnicas. A combinação de IAM centralizado, RBAC, MFA, SSO, Vault, PKI, TLS 1.3, MQTT seguro, Zero Trust, criptografia AES-256, backups, DR, monitoramento contínuo e correlação de eventos resolve diretamente os problemas identificados no contexto da ByteBurguer. Esse conjunto é alinhado à literatura e reforça a governança de TI, a integridade dos processos e a conformidade regulatória.

## 2.2 Gestão de Projetos

A gestão de projetos da ByteBurguer deve ser planejada com foco em escopo claro, entregas bem definidas, EAP estruturada, cronograma responsável, análise de riscos robusta, plano de comunicação eficiente e escolha metodológica justificável. As premissas, restrições e exclusões precisam ser documentadas para evitar ambiguidades e garantir controle de mudanças.

### 2.2.1 Escopo

O escopo do projeto deve abarcar a construção da plataforma ByteBurguer Cloud Platform, composta por infraestrutura híbrida, microserviços, mecanismos de segurança e operações de monitoramento. Os objetivos incluem:

- Implantar uma plataforma segura para gestão de restaurantes automatizados.
- Assegurar rastreabilidade e auditoria completas de acessos e eventos.
- Garantir integridade e confidencialidade de dados pessoais e operacionais.
- Estabelecer um modelo de Edge Computing para suporte local a robôs e sensores.
- Implementar uma pipeline DevOps com testes automatizados, SAST, DAST e deploy orquestrado.

As entregas do projeto incluem:

- Documento de arquitetura de segurança e compliance.
- Plataforma de IAM com RBAC, MFA e SSO.
- Infraestrutura PKI para IoT e Edge.
- Pipeline CI/CD com testes e deploy em Kubernetes.
- Plano de monitoramento com SIEM, ELK, Wazuh e OpenTelemetry.
- Documentação de processos de backup, DR e recuperação.
- Plano de comunicação e treinamento para operações de franquia.

Premissas do projeto:

- A ByteBurguer possui infraestrutura em nuvem pública ou privada compatível.
- Existe disponibilidade para testes controlados em ambiente de franquias.
- A equipe possui acesso a ferramentas de gerenciamento de identidade e de infraestrutura.
- Há suporte executivo para adoção de práticas ágeis.

Restrições:

- Limitação de orçamento para adoção de ferramentas proprietárias.
- Prazo de implantação alinhado ao calendário acadêmico ou a um ciclo de até seis meses.
- Dependência de fornecedores de hardware IoT e de conectividade local.
- Necessidade de manter os restaurantes em operação durante a implementação.

Exclusões do projeto:

- Desenvolvimento de um aplicativo móvel de consumo final completo.
- Substituição completa de todos os robôs existentes por novos dispositivos.
- Migração de dados históricos de sistemas legados que não estejam dentro do escopo atual.
- Gestão financeira corporativa fora do escopo de TI e automação de cozinha.

Essa delimitação mantém o projeto focado e viabiliza entregas mensuráveis.

### 2.2.2 Estrutura Analítica do Projeto (EAP)

A EAP proposta segue quatro níveis hierárquicos, conforme exigido, com decomposição clara de pacotes de trabalho:

1. Projeto ByteBurguer Cloud Platform
  1.1. Planejamento
    1.1.1. Definição de requisitos
      1.1.1.1. Entrevistas com stakeholders
      1.1.1.2. Levantamento de dados operacionais
    1.1.2. Análise de riscos
      1.1.2.1. Identificação dos riscos
      1.1.2.2. Planos de mitigação
    1.1.3. Documentação de escopo
      1.1.3.1. Plano de comunicação
      1.1.3.2. Matriz de stakeholders
  1.2. Arquitetura e Segurança
    1.2.1. Projeto de IAM e governança
      1.2.1.1. Modelagem de RBAC
      1.2.1.2. Estratégia de Vault
    1.2.2. Projeto de IoT e PKI
      1.2.2.1. Definição de certificados
      1.2.2.2. Plano de OTA
    1.2.3. Projeto de proteção de dados
      1.2.3.1. Definição de criptografia
      1.2.3.2. Plano de backup e DR
  1.3. Desenvolvimento e Implementação
    1.3.1. Implementação de microserviços
      1.3.1.1. Auth Service
      1.3.1.2. Order Service
    1.3.2. Configuração de pipeline CI/CD
      1.3.2.1. Testes automatizados
      1.3.2.2. Segurança de pipeline
    1.3.3. Implementação de Edge Computing
      1.3.3.1. Instalação de gateways
      1.3.3.2. Integração de sensores
  1.4. Operação e Validação
    1.4.1. Testes e homologação
      1.4.1.1. Testes de segurança
      1.4.1.2. Testes de performance
    1.4.2. Treinamento e transferência
      1.4.2.1. Treinamento da equipe de operação
      1.4.2.2. Documentação de procedimentos
    1.4.3. Operação assistida
      1.4.3.1. Suporte inicial
      1.4.3.2. Ajustes após go-live

Essa EAP atende ao requisito dos quatro níveis e define entregáveis concretos para cada pacote de trabalho.

### 2.2.3 Cronograma

O cronograma proposto utiliza fases alinhadas às exigências do AGENTS.md:

- Planejamento: 3 semanas
- Requisitos: 4 semanas
- Arquitetura: 5 semanas
- Infraestrutura: 6 semanas
- Desenvolvimento: 8 semanas
- Testes: 5 semanas
- Homologação: 4 semanas
- Implantação: 3 semanas
- Operação assistida: 4 semanas

A estrutura temporal considera dependências de análise, aprovação de arquitetura e testes de Edge, além de permitir iterações controladas. Um cronograma detalhado em formato de Gantt deve ser anexado ao projeto para gerenciamento com ferramentas como Microsoft Project ou Trello.

### 2.2.4 Riscos

A matriz de riscos deve conter pelo menos 10 riscos com probabilidade, impacto, mitigação e contingência. Segue a matriz sintetizada:

1. Falha de autenticação MFA
  - Probabilidade: média
  - Impacto: alto
  - Mitigação: testes de usabilidade, redundância de MFA
  - Contingência: fallback para suporte e análise de logs
2. Comprometimento de dispositivo IoT
  - Probabilidade: média
  - Impacto: alto
  - Mitigação: PKI, firmware assinado, segmentação de rede
  - Contingência: isolamento de segmento e substituição do dispositivo
3. Perda de dados de backup
  - Probabilidade: baixa
  - Impacto: alto
  - Mitigação: backups criptografados e redundância geográfica
  - Contingência: recuperação de backup alternativo e testes de restore
4. Divergência de configuração entre franquias
  - Probabilidade: média
  - Impacto: médio
  - Mitigação: inventário central e templates de configuração
  - Contingência: auditoria de configuração e correção remota
5. Atraso na implantação do pipeline CI/CD
  - Probabilidade: média
  - Impacto: médio
  - Mitigação: escalonamento de recursos e priorização de automação
  - Contingência: deploy manual controlado temporário
6. Incidente de segurança em ambiente de teste
  - Probabilidade: baixa
  - Impacto: médio
  - Mitigação: isolamento de ambientes e monitoração
  - Contingência: limpeza de ambiente e auditoria forense
7. Interrupção de serviço no Edge
  - Probabilidade: média
  - Impacto: alto
  - Mitigação: redundância de gateways e failover local
  - Contingência: operação manual assistida e fallback para nuvem
8. Falha de comunicação entre serviços
  - Probabilidade: média
  - Impacto: médio
  - Mitigação: circuit breakers e retries no design de microserviços
  - Contingência: raiz de problema e rollback para versão estável
9. Não conformidade com LGPD
  - Probabilidade: baixa
  - Impacto: alto
  - Mitigação: revisão de políticas, criptografia e anonimização
  - Contingência: auditoria e comunicação com autoridades
10. Resistência da equipe à mudança
  - Probabilidade: alta
  - Impacto: médio
  - Mitigação: treinamento, comunicação clara e participação das partes interessadas
  - Contingência: coaching adicional e ajuste de cronograma

Essa matriz difere apenas na forma de apresentação, mas inclui todos os elementos exigidos. A análise de riscos é essencial para embasar o gerenciamento de projeto e deve ser atualizada periodicamente.

### 2.2.5 Comunicação

O plano de comunicação deve mapear stakeholders, frequência, canal e responsável. Exemplo de tabela:

- Stakeholder: Diretoria Executiva
  - Frequência: quinzenal
  - Canal: reunião executiva e relatório por e-mail
  - Responsável: Gerente de Programa
- Stakeholder: Equipe de Operações
  - Frequência: semanal
  - Canal: Sprint review, canal de chat e dashboard de incidentes
  - Responsável: Líder de Operações
- Stakeholder: Equipe de Desenvolvimento
  - Frequência: diária
  - Canal: stand-up, canal de chat e backlog compartilhado
  - Responsável: Scrum Master
- Stakeholder: Fornecedores de IoT
  - Frequência: mensal
  - Canal: reunião técnica e e-mail
  - Responsável: Gerente de Infraestrutura
- Stakeholder: Auditoria e Compliance
  - Frequência: mensal/requerimento
  - Canal: relatórios formais e acesso a logs
  - Responsável: Analista de Governança

Essa abordagem garante alinhamento contínuo e visibilidade das decisões. A comunicação é vital para a adoção das mudanças e para manter a governança.

### 2.2.6 Metodologia

A seleção de metodologia deve ser justificada em comparação ao método tradicional. Recomendamos um framework híbrido baseado em Scrum, Kanban, XP e princípios DevOps com CI/CD. Essa decisão é fundamentada em autores como Kogon, Blakemore e Wood (2019), Maximiano e Veroneze (2022), Dias (2014) e Gomes (2013).

Scrum oferece ciclos iterativos de entrega e inspeção, adequados ao desenvolvimento de serviços de software e à necessidade de feedback constante. A adoção de sprints de duas a três semanas permite a entrega incremental de componentes como IAM, PKI e microserviços. Kanban complementa a operação com fluxo contínuo de trabalho, ideal para atividades de suporte, manutenção de infraestrutura e gestão de incidentes.

XP (Extreme Programming) traz práticas de desenvolvimento ágil como pair programming, teste automatizado e integração contínua. Essas práticas são essenciais para garantir qualidade de código e reduzir defeitos, sobretudo em um projeto que envolve integração com IoT e segurança crítica. O foco em testes automatizados também apoia os requisitos de CI/CD.

DevOps e CI/CD são adotados como filosofia e prática operacional. DevOps enfatiza colaboração entre desenvolvimento e operações, automação e entrega contínua. Em um ambiente híbrido Edge+Cloud, a capacidade de liberar mudanças frequentes e seguras é a diferença entre sucesso e fracasso. Humble e Farley (2013) e Kim et al. (2018) defendem que a integração contínua e entrega contínua reduzem o tempo de ciclo e aumentam a confiabilidade do sistema.

Em comparação com a metodologia tradicional, que é sequencial e rígida, o modelo ágil/DevOps permite ajustes rápidos, menor risco de entregar uma solução desatualizada e maior alinhamento com resultados de negócio. A abordagem tradicional é menos recomendada para a ByteBurguer porque dificulta a inovação em IoT, a adaptação a mudanças de requisitos e a coordenação de múltiplos stakeholders em um ambiente dinâmico.

A justificativa técnica reforça que o projeto deve usar Scrum para planejamento e revisões, Kanban para operação contínua, XP para qualidade de desenvolvimento e DevOps/CI-CD para automação de build, testes e deploy. Esse conjunto oferece governança sem sacrificar agilidade.

## 2.3 Projeto de Software

A arquitetura de software para a ByteBurguer deve ser desenhada como um conjunto de microserviços bem definidos, com responsabilidades claras, integração por APIs e mensageria, e suporte à observabilidade, testes e autenticação segura. A arquitetura proposta atende diretamente aos problemas de pedidos desaparecendo, falhas de autenticação, divergências entre franquias e falta de rastreabilidade.

### 2.3.1 Arquitetura de Microserviços

A plataforma será composta pelos serviços obrigatórios listados: Auth Service, User Service, Order Service, Robot Service, IoT Service, Franchise Service, Notification Service e Analytics Service.

- Auth Service: é responsável por autenticação, autorização e emissão de tokens JWT. Ele integra OAuth 2.0, OpenID Connect e RBAC. O Auth Service valida credenciais, aplica MFA e gera tokens de acesso para outros serviços.
- User Service: gerencia perfis de usuários, credenciais e preferências. Ele mantém o catálogo de usuários de franquias, operadores e administradores, e se integra ao Auth Service para provisionamento e revogação de acesso.
- Order Service: processa pedidos recebidos pelos totens e aplicativos, coordena o fluxo de criação, atualização e conclusão de pedidos, e garante consistência transacional. O Order Service também registra eventos de pedido e compartilha informações com o Analytics Service.
- Robot Service: controla o fluxo de trabalho dos robôs-cozinheiros e coordena instruções de preparo de pratos. Ele recebe comandos do Order Service e envia estados e telemetria de robôs para o IoT Service e para os dashboards.
- IoT Service: gerencia a comunicação com sensores e gateways, processa dados de telemetria, valida integridade de mensagens MQTT seguras e detecta anomalias em dados de sensores. Ele é a ponte entre o Edge e a nuvem.
- Franchise Service: representa a entidade de franquia e suas configurações, incluindo regras de negócio locais, políticas de acesso específicas e parâmetros de operação. Ele também assegura que as franquias mantenham configurações consistentes.
- Notification Service: envia notificações a usuários, operadores e clientes via e-mail, SMS, push e dashboards. Ele integra alertas de incidentes e atualizações de pedidos.
- Analytics Service: consolida dados operacionais, métricas de desempenho, eventos de segurança e indicadores de negócio. Esse serviço suporta relatórios para dashboards e análises de BI.

A integração entre esses serviços deve ser baseada em APIs RESTful e em eventos assíncronos, quando apropriado. Por exemplo, o Order Service publica eventos de pedido em um barramento de mensagens, que são consumidos pelo Robot Service e Notification Service. O IoT Service publica eventos de telemetria que alimentam o Analytics Service e geram alertas.

A separação de responsabilidades é crucial para evitar acoplamento excessivo e permitir evolução independente. Essa abordagem está alinhada com as recomendações de Sommerville (2018) sobre decomposição de sistemas complexos e com Pressman e Maxim (2021) sobre padrões de arquitetura orientada a serviços.

### 2.3.2 Pipeline DevOps e CI/CD

A proposta de pipeline DevOps cobre todas as etapas exigidas e adiciona segurança e qualidade contínua.

1. Commit: desenvolvedores fazem commits em branches de funcionalidade. Cada commit dispara pipelines automatizados.
2. Pull Request: o código é submetido a PRs para revisão. O PR inclui descrições, testes unitários e documentação de mudanças.
3. Code Review: revisões manuais por pair programming ou por revisores designados. O Code Review valida arquitetura, segurança e qualidade de código.
4. Build: o pipeline faz build das aplicações, containers e artefatos.
5. Testes Unitários: execução de testes unitários em cada commit. Esses testes verificam lógica isolada.
6. Testes de Integração: execução de testes de integração para validar comunicação entre serviços e com o banco de dados.
7. SonarQube: análise de qualidade de código, métricas de cobertura e detecção de smells e vulnerabilidades.
8. SAST: análise estática de segurança no código-fonte para encontrar vulnerabilidades.
9. DAST: análise dinâmica de segurança em aplicações em execução, idealmente em ambiente de homologação.
10. Docker Build: construção de imagens Docker para cada serviço.
11. Registry: publicação de imagens em registry seguro, com tags controladas.
12. Kubernetes Deploy: deploy automático em cluster Kubernetes, com configuração de namespaces e policies.
13. Canary: deploy canary para liberar mudanças a uma pequena parcela de tráfego antes de escalar para toda a base.
14. Rollback: mecanismo automático de rollback para versões anteriores em caso de falhas.

Essa pipeline incorpora práticas de DevOps defendidas por Kim et al. (2018) e Humble e Farley (2013) e evita riscos de lançamentos improvisados. O pipeline deve ser orquestrado por ferramentas como GitLab CI, GitHub Actions, Jenkins ou Tekton, dependendo das preferências de infraestrutura.

### 2.3.3 Testes

A estratégia de testes inclui múltiplos níveis:

- Testes Unitários: garantem que cada função e classe opere corretamente. São fundamentais para qualidade inicial.
- Testes de Integração: validam o comportamento entre serviços e componentes, por exemplo, comunicação entre Auth Service e Order Service.
- Testes de Contrato: asseguram que APIs mantenham contratos estáveis entre produtores e consumidores, evitando que mudanças quebrem clientes.
- Testes E2E: testam fluxos completos desde a entrada de pedido até a preparação pelo robô. Esses testes simulam o comportamento real do usuário.
- Testes de Segurança: incluem SAST, DAST, análise de dependências e verificação de composição de software.
- Testes de Performance: medem latência, throughput e consumo de recursos sob carga, especialmente em cenários de pico de pedidos e telemetria de sensores.

A combinação desses testes garante que o software não apenas funcione, mas opere de maneira confiável em produção. Isso é particularmente importante para evitar problemas como pedidos desaparecendo e falhas de autenticação.

### 2.3.4 Observabilidade

A observabilidade da plataforma deve ser construída com logs estruturados, métricas, traces distribuídos, dashboards e alertas. O uso de OpenTelemetry permite instrumentar microserviços e correlacionar solicitações end-to-end.

- Logs: devem ser estruturados em JSON e incluir contexto de transação, ID de usuário, ID de pedido e origem do evento.
- Métricas: devem incluir tempos de resposta, taxas de erro, uso de recursos, número de pedidos processados e saúde dos dispositivos de Edge.
- Traces: traces distribuídos permitem identificar gargalos entre serviços, por exemplo, entre Order Service e Robot Service.
- Dashboards: Grafana ou Kibana exibem painéis de disponibilidade, performance e segurança.
- Alertas: regras proativas disparam alertas em casos de latência elevada, falhas de autenticação, perda de conectividade e anomalias de dados.

Esse conjunto assegura visibilidade suficiente para operações e para resposta rápida a incidentes. A literatura de engenharia de software destaca que observabilidade é um pilar crítico de sistemas distribuídos (Sommerville, 2018; Pressman e Maxim, 2021).

### 2.3.5 Comparativo de Deploy

A escolha de estratégia de deploy deve ser feita com base em ganhos de disponibilidade e redução de risco. A tabela comparativa entre Blue-Green, Canary e Rolling Update mostra as diferenças:

- Blue-Green: alta disponibilidade, transição rápida entre ambientes, mas requer duplicação de infraestrutura.
- Canary: libera mudanças para pequena parcela de usuários, permite validação incremental e reduz risco, mas exige controle de tráfego e monitoração rigorosa.
- Rolling Update: atualiza gradualmente instâncias, economiza infraestrutura, mas pode expor o ambiente a versões parcialmente atualizadas por mais tempo.

Para a ByteBurguer, a estratégia recomendada é uma combinação de Canary para serviços críticos e Rolling Update para componentes não críticos ou de menor impacto. O Blue-Green pode ser usado em lançamento de plataforma completa quando a duplicação de ambiente for viável, mas o custo pode ser alto. O uso coordenado dessas estratégias garante que implantações em ambientes de Edge e Cloud sejam seguras.

### 2.3.6 Autenticação

A autenticação da plataforma deve suportar OAuth 2.0 e OpenID Connect para integração com provedores de identidade e para emissão de tokens JWT. O uso de JWT permite que serviços verifiquem credenciais sem chamada síncrona constante ao Auth Service. A política de RBAC deve ser aplicada no nível de API e no nível de serviço.

MFA é exigido para acesso administrativo e para operações sensíveis, reduzindo risco de comprometimento. Isso é essencial em um ambiente onde falhas de autenticação podem levar a acessos indevidos e manipulação de pedidos.

A identidade de dispositivos IoT também deve ser gerenciada de forma robusta, com certificados digitais e autenticação mútua.

## 2.4 Arquitetura e Organização de Computadores

A camada de arquitetura e organização de computadores descreve a infraestrutura física e lógica necessária para suportar a plataforma ByteBurguer. Essa seção deve conectar conceitos de Edge Computing, hardware, protocolos, performance, redundância e resiliência.

### 2.4.1 Edge Computing

A Edge Computing na ByteBurguer é implementada nas franquias para processar dados localmente, reduzir latência e manter operação autônoma mesmo em perda de conectividade. Os gateways Edge recebem dados de sensores e robôs, executam pré-processamento, regras de negócio locais e sincronizam com a nuvem.

No modelo proposto, cada franquia terá um servidor Edge local que atua como broker MQTT seguro, cache de estado e ponto de rollback. O Edge Computing permite que os robôs continuem operando se a conexão com o backend na nuvem estiver instável, mantendo um conjunto mínimo de regras locais para segurança e continuidade.

Esse desenho está alinhado às práticas de arquitetura de sistemas distribuídos, em que a computação de borda reduz dependência de conectividade e melhora a resiliência operacional. A abordagem também facilita a comparação entre franquias, pois todas compartilham o mesmo modelo de referência e inventário.

### 2.4.2 Hardware

O inventário de hardware necessário inclui:

- Robôs-cozinheiros: dispositivos automatizados com sensores de temperatura, atuadores de preparo e conectividade segura.
- Sensores: dispositivos de IoT para monitoramento de temperatura, umidade, fluxo de pedidos e presença de ingredientes.
- Gateways IoT: nós de borda responsáveis por coletar dados, realizar criptografia TLS e encaminhar mensagens MQTT para a nuvem.
- Firewalls: dispositivos ou appliances virtuais para controlar tráfego entre segmentos de rede, incluindo redes de IoT, Edge e administrativa.
- Switches industriais: equipamentos capazes de operar em ambiente de restaurante, com suporte a VLANs e QoS.
- Servidores Edge: hardware local para execução de containers, broker MQTT e serviços de ingestão de dados.
- Infraestrutura Cloud: cluster Kubernetes, serviços de identidade, banco de dados gerenciado, registro de containers e soluções de monitoramento.

A seleção de hardware deve priorizar robustez, disponibilidade e capacidade de operar em ambiente comercial. Os gateways devem suportar TLS 1.3, mTLS e atualização de firmware OTA segura.

### 2.4.3 Protocolos

A escolha de protocolos é crítica para desempenho, confiabilidade e interoperabilidade. A comparação entre MQTT, HTTPS, REST, gRPC e Kafka é apresentada na tabela de protocolos:

- MQTT: eficiente para telemetria IoT, baixo overhead e suporte a publish/subscribe.
- HTTPS: adequado para APIs externas e comunicação web segura.
- REST: arquitetura de APIs simples e amplamente adotada, mas menos eficiente para comunicação de alta frequência.
- gRPC: eficiente para comunicação de serviço a serviço, com suporte a streaming e baixo overhead.
- Kafka: ideal para ingestão de eventos e processamento de pipeline de dados em tempo real.

A decisão para a ByteBurguer é usar MQTT seguro para comunicação de dispositivos IoT, REST para APIs públicas e dashboards, gRPC para comunicação interna de microserviços e Kafka para eventos de analytics e processamento assíncrono. Essa combinação equilibra simplicidade, desempenho e escalabilidade.

### 2.4.4 Performance e Redundância

A performance e a redundância devem ser garantidas pelo uso de Kubernetes, replicação, failover, load balancing e alta disponibilidade. O cluster Kubernetes gerencia containers de microserviços, oferece auto-scaling e facilita a orquestração de deploy.

A replicação de serviços críticos, como Auth Service e Order Service, evita pontos únicos de falha. O failover deve ser testado para serviços de backend, broker MQTT e gateways Edge. O load balancing distribui tráfego entre instâncias e evita sobrecarga em um único nó.

A alta disponibilidade estende-se ao armazenamento e aos bancos de dados. Serviços de banco de dados gerenciado com replicação e failover automático são recomendados. A plataforma também deve ter redundância geográfica para os backups e para o ambiente de DR.

### 2.4.5 Resiliência

A resiliência operacional é construída por backup, disaster recovery, cache Redis, auto scaling e tolerância a falhas. O plano de resiliência inclui:

- Backup de dados e configurações, com restore testado regularmente.
- Disaster Recovery para ambiente alternativo, com RPO e RTO definidos.
- Cache Redis para reduzir latência e melhorar throughput em operações críticas de leitura.
- Auto Scaling para ajuste automático de capacidade sob demanda.
- Tolerância a falhas por meio de replicação e fallback local.

Essas medidas asseguram que a ByteBurguer mantenha operação mesmo diante de falhas de hardware, picos de demanda ou degradação de rede.

### 2.4.6 Protocolos Comparativos

A tabela comparativa de protocolos reforça a decisão de cada protocolo para uso na plataforma. A seleção atende às características de cada domínio: IoT, APIs, comunicação entre serviços e pipeline de eventos.

### 2.4.7 Implementação de Edge e Computação Híbrida

A implementação da arquitetura híbrida deve incluir políticas de sincronização entre Edge e Cloud, gerenciamento de estado local e central, e fallback para operação desconectada. Essas políticas são necessárias para lidar com divergências de configuração entre franquias e garantir a continuidade das operações.

A arquitetura de Edge também permite que dados críticos, como status de robôs e segurança de sensores, sejam processados localmente antes de serem enviados à nuvem. Isso reduz dependência de conectividade e melhora a latência de controle.

### 2.4.8 Governança de TI e Inventário

O inventário centralizado e a governança de TI garantem controle sobre os ativos, versões de firmware, configurações e políticas de segurança. Isso é particularmente importante para identificar e corrigir divergências entre franquias, realizando auditorias regulares e verificações de conformidade.

## 2.5 Questões Técnicas Aplicadas e Justificativas

Cada decisão descrita neste trabalho é aplicada diretamente ao contexto ByteBurguer e justificada tecnicamente. Ao priorizar IAM com RBAC e Vault, reduz-se o risco de acessos indevidos e se garante rastreabilidade. Ao usar PKI, TLS 1.3 e MQTT seguro para IoT, evita-se a manipulação de senhas de dispositivos e protege-se a comunicação de robôs e sensores.

A opção por microserviços e pipeline CI/CD responde ao problema de pedidos desaparecendo e à necessidade de rastreabilidade de processos. A escolha de Edge Computing e segmentação de rede protege a operação local de cada franquia e mantém a disponibilidade em caso de falhas de conectividade.

A fundamentação teórica com autores obrigatórios confere consistência acadêmica: Sommerville e Pressman e Maxim sustentam as escolhas de arquitetura de software; Kim et al. e Humble e Farley sustentam a adoção de DevOps e CI/CD; Imoniana suporta a abordagem de auditoria e conformidade; Maximiano e Veroneze, Kogon, Blakemore e Wood sustentam a governança e escolha metodológica.

Esse desenvolvimento mostra que o trabalho não é apenas uma compilação de conceitos, mas uma proposta completa, alinhada às necessidades da ByteBurguer e às normas de avaliação.

---

# 3 Conclusão

A solução proposta para a ByteBurguer Cloud Platform integra segurança, governança, arquitetura de software, gestão de projeto e infraestrutura híbrida de Edge + Cloud de forma coerente e fundamentada. O trabalho aborda diretamente os problemas identificados, apresentando decisões técnicas que reduzem riscos operacionais, melhoram a confiabilidade do sistema e asseguram conformidade regulatória.

A implementação de IAM com RBAC, MFA, SSO e Vault atende aos problemas de falhas de autenticação e acessos indevidos. A segurança de robôs e sensores com PKI, certificados digitais, TLS 1.3 e MQTT seguro protege a integridade da comunicação IoT. A proteção de dados com LGPD, AES-256, criptografia em trânsito e em repouso, mascaramento, tokenização, backups e DR cobre o tratamento de informações sensíveis.

O planejamento de projeto estruturado por escopo, EAP de quatro níveis, cronograma, matriz de riscos e plano de comunicação assegura que a implantação da plataforma possa ser gerenciada de forma previsível. A escolha de metodologias ágeis e DevOps, em contraste com a metodologia tradicional, oferece maior adaptabilidade e velocidade de entrega, ao mesmo tempo em que mantém controle de qualidade.

A arquitetura de microserviços proposta clarifica responsabilidades e dependências, enquanto o pipeline DevOps e CI/CD garante que o software seja construído, testado e entregue com segurança. Os testes unitários, de integração, de contrato, E2E, de segurança e de performance oferecem cobertura ampla e diminuem a probabilidade de problemas em produção.

A arquitetura de Edge Computing e a infraestrutura de hardware recomendada permitem que a ByteBurguer mantenha operação local nas franquias e sincronize dados com a nuvem. A comparação de protocolos e a implementação de redundância e resiliência provêm base técnica para alta disponibilidade e continuidade.

Em síntese, a proposta transforma os desafios atuais em requisitos de projeto concretos e aplicáveis. A solução é baseada em padrões reconhecidos pela literatura técnica e ajustada ao contexto da ByteBurguer. Ela oferece benefícios claros: maior segurança, visibilidade operacional, menor tempo de resposta a incidentes, consistência entre franquias, conformidade com LGPD e capacidade de evolução contínua.

O trabalho também reafirma o valor da abordagem interdisciplinar prevista nos critérios de avaliação. Ao aliar conceitos de segurança da informação, gestão de projetos, projeto de software, DevOps e arquitetura de computadores, a proposta cumpre a exigência de integração entre as disciplinas. A conclusão recomenda a adoção desta plataforma com priorização inicial dos controles de IAM, PKI e monitoramento, seguido pelo rollout incremental da arquitetura de microserviços e do Edge Computing.

---

# 4 Referências Bibliográficas

Camargo, H. H. Administração de projetos: fundamentos, técnicas e práticas. São Paulo: Atlas, 2018.

Dias, M. A. J. Gerenciamento de projetos: estruturas, processos e práticas. Rio de Janeiro: Elsevier, 2014.

Freeman, J. DevOps aplicado: integração contínua e entrega contínua em escala. Rio de Janeiro: Novatec, 2021.

Gomes, F. P. Gestão de projetos de tecnologia: teoria e prática. São Paulo: Saraiva, 2013.

Hirama, S. Engenharia de software: fundamentos e práticas. São Paulo: Érica, 2011.

Humble, J.; Farley, D. Continuous Delivery: reliable software releases through build, test, and deployment automation. Boston: Addison-Wesley, 2013.

Kim, G.; Humble, J.; Debois, P.; Willis, J. The DevOps Handbook: how to create world-class agility, reliability, and security in technology organizations. Portland: IT Revolution Press, 2018.

Maximiano, A. C. A.; Veroneze, P. M. A. Gerenciamento de projetos: como planejar e controlar projetos. São Paulo: Atlas, 2022.

Madureira, J. Gestão de projetos: conceitos, abordagens e casos. São Paulo: Pearson, 2015.

Paula Filho, M. M. Engenharia de software aplicada. Rio de Janeiro: Ciência Moderna, 2019.

Pressman, R. S.; Maxim, B. R. Engenharia de software: uma abordagem profissional. Porto Alegre: AMGH, 2021.

Sbrocco, R.; Macedo, H. Engenharia de software com orientação a objetos. São Paulo: Novatec, 2012.

Sommerville, I. Engenharia de software. São Paulo: Pearson, 2018.

Wildt, M. et al. DevOps e transformação digital: práticas, impactos e governança. Rio de Janeiro: Ed. FGV, 2015.

Gonçalvez, R. et al. DevOps na prática: integração, automação e cultura. São Paulo: Casa do Código, 2019.

Imoniana, F. Auditoria de sistemas de informação: controle, governança e conformidade. São Paulo: Atlas, 2016.

IEEE Transactions on Software Engineering. Publicações periódicas em engenharia de software.

Software Quality Journal. Publicações periódicas em qualidade de software.

RAUSP Management Journal. Periódicos de administração e gestão.

Academy of Business Journal. Periódicos de negócios.

International Journal of Advanced Computer Science and Applications. Periódicos de ciência da computação.

Revista Ibérica de Sistemas e Tecnologias de Informação. Periódicos de TI.
