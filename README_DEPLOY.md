Projeto scaffold para ByteBurguer Cloud Platform

Como usar (Docker Compose - local):

1. Copie o exemplo de env:

```bash
cp .env.example .env
```

2. Build e subir todos os serviços:

```bash
make up
```

3. Verificar logs:

```bash
make logs
```

Endpoints (exemplos):
- Auth: http://localhost:5100/health
- Order: http://localhost:5101/health
- Robot: http://localhost:5102/health
- IoT: http://localhost:5103/health
- Franchise: http://localhost:5104/health
- Notification: http://localhost:5105/health
- Analytics: http://localhost:5106/health
- User: http://localhost:5107/health

Subir para produção (exemplo rápido):
- Configure um registry (Docker Hub / GHCR)
- Atualize `docker-compose.yml` ou crie manifests Kubernetes
- Use GitHub Actions (arquivo .github/workflows/ci.yml) para build/push

Observações:
- Este scaffold fornece serviços mínimos para testes e integração. Substitua por implementações reais conforme especificado no trabalho acadêmico.
