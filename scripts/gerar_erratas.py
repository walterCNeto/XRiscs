"""Gera erratas.md juntando as seções de erratas e notas de cada notebook.

Uso (na raiz do repositório): python scripts/gerar_erratas.py
"""
import glob
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CABECALHO = r"(Erratas|Notas) (do livro|e notas|sobre)"

partes = []
for caminho in sorted(glob.glob(str(RAIZ / "[0-9][0-9]_*.ipynb"))):
    nb = json.loads(Path(caminho).read_text(encoding="utf-8"))
    titulo = None
    secao = []
    for celula in nb["cells"]:
        if celula["cell_type"] != "markdown":
            continue
        texto = "".join(celula["source"])
        if titulo is None and texto.startswith("# "):
            titulo = texto.splitlines()[0][2:].strip()
        linhas = texto.splitlines()
        dentro = False
        for linha in linhas:
            if linha.startswith("## "):
                dentro = bool(re.search(CABECALHO, linha))
                continue
            if dentro:
                secao.append(linha)
    corpo = "\n".join(secao).strip()
    if corpo:
        nome = Path(caminho).stem
        partes.append(f"## {titulo}\n\nNotebook: [{nome}]({nome}.ipynb)\n\n{corpo}\n")

texto = """# Erratas e notas sobre o livro

Esta página junta, módulo a módulo, as erratas e observações registradas nos notebooks. Cada item foi
conferido numericamente no laboratório correspondente. O livro de referência é *Derivatives Analytics
with Python* (Y. Hilpisch, Wiley, 2015); as seções e equações citadas são as do livro.

Página gerada automaticamente por `scripts/gerar_erratas.py`.

""" + "\n".join(partes)
(RAIZ / "erratas.md").write_text(texto, encoding="utf-8")
print(f"erratas.md: {len(partes)} módulos")
