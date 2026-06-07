# ByteBurguer Cloud Platform - Trabalho Acadêmico

Arquivo principal:

- `ByteBurguer_Cloud_Platform_Academico_Final.md`

Este documento atende aos requisitos do AGENTS.md, incluindo:

- Estrutura ABNT com capa, folha de rosto, sumário, introdução, desenvolvimento, conclusão e referências.
- Seções com mais de 1200 palavras cada.
- Fundamentação teórica explícita com os autores exigidos.
- Abordagem integrada de Segurança, Gestão de Projetos, Projeto de Software e Arquitetura de Computadores.

## Como gerar PDF

O ambiente atual não possui `pandoc` nem bibliotecas Python de conversão instaladas. Para gerar PDF localmente, use uma das opções abaixo:

### Usando Pandoc

```bash
sudo apt install pandoc texlive-xetex
cd /home/diego/dev/devops-faculdade/1
pandoc ByteBurguer_Cloud_Platform_Academico_Final.md -o ByteBurguer_Cloud_Platform_Academico_Final.pdf
```

### Usando VS Code

1. Abra `ByteBurguer_Cloud_Platform_Academico_Final.md`.
2. Use a pré-visualização do Markdown (`Ctrl+Shift+V`).
3. Exporte para PDF com uma extensão de Markdown ou usando a opção de impressão do VS Code.

### Usando Python (se instalado)

Instale pacotes necessários:

```bash
pip install markdown2 weasyprint
```

E então execute:

```bash
python3 - <<'PY'
from pathlib import Path
import markdown2
from weasyprint import HTML

source = Path('ByteBurguer_Cloud_Platform_Academico_Final.md').read_text(encoding='utf-8')
html = markdown2.markdown(source)
HTML(string=html).write_pdf('ByteBurguer_Cloud_Platform_Academico_Final.pdf')
PY
```

## Observação

O arquivo `ByteBurguer_Cloud_Platform_Academico_Final.md` já está pronto para revisão e entrega. Se você quiser, posso também preparar uma versão final em LaTeX ou converter o arquivo em PDF assim que a ferramenta apropriada estiver disponível.
# PROJETO-INTEGRADO-S-NTESE---DEVOPS
