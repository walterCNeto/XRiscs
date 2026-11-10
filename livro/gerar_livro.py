"""Gera o livro em PDF (XeLaTeX) a partir dos notebooks executados do XRiscs.

Uso (na raiz do repositório):  python livro/gerar_livro.py
Requisitos: pandoc, XeLaTeX (TeX Live com polyglossia/portuguese), latexmk, beautifulsoup4.
Saída: livro/XRiscs_Derivativos_com_Python.pdf
"""
import base64
import datetime as dt
import re
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

import nbformat
import yaml
from bs4 import BeautifulSoup

RAIZ = Path(__file__).resolve().parents[1]
LIVRO = RAIZ / "livro"
BUILD = Path(tempfile.gettempdir()) / "xriscs_livro"
FIGS = BUILD / "figs"
SAIDA_PDF = LIVRO / "XRiscs_Derivativos_com_Python.pdf"
TEORIA = LIVRO / "teoria"
SITE = "https://waltercneto.github.io/XRiscs"
MAX_LINHAS_SAIDA = 45
SUP = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ", "0123456789-+n"))
SUB = dict(zip("₀₁₂₃₄₅₆₇₈₉", "0123456789"))
# símbolos sem glifo na Latin Modern (texto): viram matemática
MATH_TXT = {"≈": r"\approx", "≤": r"\le", "≥": r"\ge", "≠": r"\neq", "→": r"\to", "←": r"\leftarrow",
            "↔": r"\leftrightarrow", "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow", "×": r"\times", "±": r"\pm",
            "−": "-", "·": r"\cdot", "√": r"\surd", "∝": r"\propto", "∞": r"\infty", "∫": r"\int", "∂": r"\partial",
            "∈": r"\in", "∼": r"\sim", "≡": r"\equiv", "⊂": r"\subset", "∑": r"\sum", "∏": r"\prod", "′": "'",
            "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ζ": r"\zeta",
            "η": r"\eta", "θ": r"\theta", "ϑ": r"\vartheta", "κ": r"\kappa", "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu",
            "ξ": r"\xi", "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau", "φ": r"\varphi", "ϕ": r"\phi",
            "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega", "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta",
            "Λ": r"\Lambda", "Π": r"\Pi", "Σ": r"\Sigma", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega", "ℓ": r"\ell"}
RE_MATH_TXT = re.compile("[" + "".join(MATH_TXT) + "]")

# blocos do cabeçalho padrão que se repetem em todos os notebooks (vão para o Apêndice A)
CABECALHO = ("AZUL, LARANJA", "MAGENTA =", "plt.rcParams.update", "def f3(", "def tabela(", "_checks =", "def ok(")


def latex_esc(s):
    s = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ]+", lambda m: "\x00SUP" + "".join(SUP[c] for c in m.group(0)) + "\x00", s)
    s = re.sub("[₀₁₂₃₄₅₆₇₈₉]+", lambda m: "\x00SUB" + "".join(SUB[c] for c in m.group(0)) + "\x00", s)
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    s = "".join(rep.get(c, c) for c in s)
    s = RE_MATH_TXT.sub(lambda m: "\\(" + MATH_TXT[m.group(0)] + "\\)", s)
    s = re.sub("\x00SUP([^\x00]*)\x00", r"\\textsuperscript{\1}", s)
    return re.sub("\x00SUB([^\x00]*)\x00", r"\\textsubscript{\1}", s)


def bloco_latex(tex):
    return f"\n\n```{{=latex}}\n{tex}\n```\n\n"


def saida_verbatim(texto):
    linhas = texto.rstrip("\n").split("\n")
    if len(linhas) > MAX_LINHAS_SAIDA:
        linhas = linhas[:MAX_LINHAS_SAIDA] + [f"[... {len(linhas) - MAX_LINHAS_SAIDA} linhas omitidas ...]"]
    linhas = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in linhas]
    return bloco_latex("\\begin{saida}\n\\begin{Saida}\n" + "\n".join(linhas) + "\n\\end{Saida}\n\\end{saida}")


def html_para_tabela(html):
    """Converte a tabela HTML do pandas (já formatada pela função tabela) em booktabs."""
    soup = BeautifulSoup(html, "html.parser")
    tab = soup.find("table")
    if tab is None:
        return None
    cab = [[c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])] for tr in tab.find("thead").find_all("tr")] if tab.find("thead") else []
    corpo = [[c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])] for tr in (tab.find("tbody") or tab).find_all("tr")]
    if not corpo:
        return None
    ncol = max(len(r) for r in corpo + cab)
    cab = [r + [""] * (ncol - len(r)) for r in cab]
    corpo = [r + [""] * (ncol - len(r)) for r in corpo]
    # índice trivial 0..n-1 sai
    if [r[0] for r in corpo] == [str(i) for i in range(len(corpo))]:
        cab = [r[1:] for r in cab]
        corpo = [r[1:] for r in corpo]
        ncol -= 1
    cab = [r for r in cab if any(x for x in r)]
    num = re.compile(r"^[−\-+]?[\d.]*\d(,\d+)?%?$|^n/d$")
    alin = "".join("r" if all(num.match(r[j]) or r[j] == "" for r in corpo) else "l" for j in range(ncol))
    out = ["\\begin{tabular}{@{}" + alin + "@{}}", "\\toprule"]
    for r in cab:
        out.append(" & ".join("\\textbf{" + latex_esc(x) + "}" for x in r) + r" \\")
    if cab:
        out.append("\\midrule")
    for r in corpo:
        out.append(" & ".join(latex_esc(x) for x in r) + r" \\")
    out += ["\\bottomrule", "\\end{tabular}"]
    return bloco_latex("\\tabelalivro{" + "\n".join(out) + "}")


def limpar_cabecalho(src):
    """Tira do código os blocos repetidos do cabeçalho padrão."""
    if "def ok(" not in src:
        return src, False
    blocos = re.split(r"\n(?=[A-Za-z_#@])", src)   # blocos de nível superior
    fica, i = [], 0
    while i < len(blocos):
        b = blocos[i]
        if b.startswith(CABECALHO):
            i += 1
            continue
        fica.append(b)
        i += 1
    texto = "\n".join(fica)
    texto = re.sub(r"\n{3,}", "\n\n", texto).strip()
    return "# Preparação padrão (cores, gráficos, f3, tabela e ok): ver Apêndice A.\n" + texto, True




def indices_unicode(texto):
    """Troca sobrescritos e subscritos Unicode (fora de fórmulas) por math; a fonte do texto não os tem."""
    pedacos = re.split(r"(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`)", texto, flags=re.S)
    for k in range(1, len(pedacos), 2):          # fórmulas inline longas: deixar quebrar nas vírgulas
        f = pedacos[k]
        if f.startswith("$") and not f.startswith("$$") and len(f) > 30:
            pedacos[k] = f.replace(", ", ",\\allowbreak ")
    for k in range(0, len(pedacos), 2):
        p = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ]+", lambda m: "$^{" + "".join(SUP[c] for c in m.group(0)) + "}$", pedacos[k])
        p = re.sub("[₀₁₂₃₄₅₆₇₈₉]+", lambda m: "$_{" + "".join(SUB[c] for c in m.group(0)) + "}$", p)
        pedacos[k] = RE_MATH_TXT.sub(lambda m: "$" + MATH_TXT[m.group(0)] + "$", p)
    return "".join(pedacos)


def markdown_celula(src, n_cap):
    src = indices_unicode(src)
    src = re.sub(r"\[([^\]]+)\]\((\d\d_[a-z0-9_]+|erratas)\)", r"\1", src)       # links entre notebooks
    src = re.sub(r"<details>\s*<summary>\s*Solução\s*</summary>(.*?)</details>",
                 lambda m: bloco_latex("\\begin{solucao}") + m.group(1).strip() + bloco_latex("\\end{solucao}"),
                 src, flags=re.S)
    src = re.sub(r"</?(sub|sup|b|br)\s*/?>", "", src)
    src = src.replace("\\[", "$$").replace("\\]", "$$") if "\\[" in src and "$$" not in src else src
    return src


def capitulo(arquivo, n_cap, cabecalho_ref):
    nb = nbformat.read(arquivo, 4)
    partes = []
    k_fig = 0
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            src = cell.source
            m = re.match(r"#\s+Módulo\s+\d+\s+[—-]\s+(.*)", src)
            if m:
                src = src.replace(m.group(0), f"# {m.group(1).strip()} {{#cap-{n_cap}}}", 1)
            if "**Curso:**" in src and (TEORIA / f"{n_cap:02d}.tex").exists():
                # ordem no livro: título, introdução, fundamentos teóricos e só então o roteiro do curso
                antes, depois = src.split("**Curso:**", 1)
                partes.append("\n\n" + markdown_celula(antes, n_cap) + "\n\n")
                partes.append(bloco_latex(f"\\aberturateoria\n\\input{{teoria/{n_cap:02d}.tex}}"))
                src = "## Roteiro do capítulo\n\n**Curso:**" + depois
            partes.append("\n\n" + markdown_celula(src, n_cap) + "\n\n")
            continue
        if cell.cell_type != "code":
            continue
        tags = cell.metadata.get("tags", [])
        src = cell.source
        if "_WIDGET" in src and "hide-input" in tags:
            partes.append(bloco_latex(
                "\\begin{nota}\\sffamily\\small\\textbf{Widget interativo.} Na versão on-line deste capítulo, esta célula "
                "mostra um construtor interativo da árvore implícita, que roda no próprio navegador. Acesse "
                f"\\url{{{SITE}/{arquivo.stem}.html}}.\\end{{nota}}"))
            continue
        src, eh_cab = limpar_cabecalho(src)
        if eh_cab and not cabecalho_ref:
            cabecalho_ref.append(cell.source)
        if src.strip():
            partes.append(f"\n\n```python\n{src}\n```\n\n")
        for o in cell.get("outputs", []):
            if o.output_type == "stream":
                partes.append(saida_verbatim(o.text))
            elif o.output_type in ("display_data", "execute_result"):
                d = o.get("data", {})
                if "image/png" in d:
                    k_fig += 1
                    nome = f"cap{n_cap:02d}_{k_fig:02d}.png"
                    (FIGS / nome).write_bytes(base64.b64decode(d["image/png"]))
                    larg = 0.95 if "figsize" not in src else 0.95
                    partes.append(bloco_latex(f"\\figura{{figs/{nome}}}{{{larg}}}"))
                elif "text/html" in d and "dkc-widget" not in d["text/html"]:
                    tab = html_para_tabela(d["text/html"])
                    partes.append(tab if tab else saida_verbatim(d.get("text/plain", "")))
                elif "text/plain" in d and "dkc-widget" not in d.get("text/html", ""):
                    partes.append(saida_verbatim(d["text/plain"]))
            elif o.output_type == "error":
                partes.append(saida_verbatim("\n".join(o.traceback)))
    return "".join(partes)


def capa(destino, seed=1973):
    """Fundo da capa: trajetórias de um movimento browniano geométrico com bandas de ±1 e ±2 desvios."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.default_rng(seed)
    W, H = 7.0, 10.0
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("#1B2E4B")
    fig.patch.set_facecolor("#1B2E4B")
    n, I, T, sig, mu = 700, 140, 1.0, 0.32, 0.04
    t = np.linspace(0, T, n + 1)
    z = rng.standard_normal((I, n)) * np.sqrt(T / n)
    x = np.concatenate([np.zeros((I, 1)), np.cumsum((mu - 0.5 * sig**2) * T / n + sig * z, axis=1)], axis=1)
    x0, y0, esc_x, esc_y = 0.06, 0.36, 0.92, 0.29     # posição na página (fração)
    X = x0 + esc_x * t / T
    m = (mu - 0.5 * sig**2) * t
    for i in range(I):
        ax.plot(X, y0 + esc_y * x[i], color="#7FB2EE", alpha=0.10, lw=0.6)
    for k, a in [(1, 0.55), (2, 0.35)]:
        for sgn in (1, -1):
            ax.plot(X, y0 + esc_y * (m + sgn * k * sig * np.sqrt(t)), color="white", alpha=a, lw=0.9, ls=(0, (4, 3)))
    for i, cor in [(int(np.argmax(x[:, -1])), "#EB6834"), (int(np.argsort(x[:, -1])[I // 2]), "#FFFFFF")]:
        ax.plot(X, y0 + esc_y * x[i], color=cor, alpha=0.95, lw=1.3)
    ax.plot([x0, x0 + esc_x], [y0 - 0.33, y0 - 0.33], color="white", alpha=0.25, lw=0.6)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.savefig(destino, facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    if BUILD.exists():
        shutil.rmtree(BUILD)
    FIGS.mkdir(parents=True)
    shutil.copytree(TEORIA, BUILD / "teoria")
    shutil.copy(LIVRO / "referencias.bib", BUILD / "referencias.bib")
    capa(BUILD / "capa_fundo.pdf")
    toc = yaml.safe_load((RAIZ / "_toc.yml").read_text(encoding="utf-8"))
    md = []
    # prefácio a partir do intro.md
    intro = (RAIZ / "intro.md").read_text(encoding="utf-8")
    intro = re.sub(r"^# .*\n", "", intro)
    intro = re.sub(r"```\{admonition\}.*?```\n*", "", intro, flags=re.S)
    intro = re.sub(r"\[([^\]]+)\]\((\d\d_[a-z0-9_]+|erratas)\)", r"\1", intro)
    intro = intro.replace("Cada módulo é um notebook", "Cada módulo é um notebook, e cada notebook é um capítulo deste livro")
    md.append("# Prefácio {-}\n\n" + indices_unicode(intro) + "\n\n" + bloco_latex("\\mainmatter"))
    cab_ref, n_cap = [], 0
    for parte in toc["parts"]:
        if parte["caption"] == "Referência":
            continue
        md.append(bloco_latex(f"\\part{{{latex_esc(parte['caption'])}}}"))
        for ch in parte["chapters"]:
            n_cap += 1
            print("capítulo", n_cap, ch["file"], flush=True)
            md.append(capitulo(RAIZ / f"{ch['file']}.ipynb", n_cap, cab_ref))
    # apêndices
    md.append(bloco_latex("\\appendix"))
    md.append("# Preparação padrão dos laboratórios {#apA}\n\nTodos os capítulos começam com a mesma célula de preparação: "
              "cores, estilo dos gráficos, a função `f3` (três casas decimais no padrão brasileiro), a função `tabela` e a função `ok`, "
              "que interrompe o notebook se uma verificação falhar. Ela aparece aqui uma vez; nos capítulos, só as partes específicas de cada um.\n\n"
              f"```python\n{cab_ref[0] if cab_ref else ''}\n```\n\n")
    err = (RAIZ / "erratas.md").read_text(encoding="utf-8")
    err = re.sub(r"^# .*\n", "# Erratas e notas sobre o livro de Hilpisch\n", err, count=1)
    err = re.sub(r"\[([^\]]+)\]\((\d\d_[a-z0-9_]+)\)", r"\1", err)
    md.append(indices_unicode(err))
    (BUILD / "livro.md").write_text("\n".join(md), encoding="utf-8")

    verif = sum(int(m) for m in re.findall(r"Módulo \d+ concluído: (\d+) verificações",
                                           "".join(nbformat.reads(Path(RAIZ / f).read_text(encoding="utf-8"), 4).cells[-1].outputs[0].get("text", "")
                                                   for f in sorted(p.name for p in RAIZ.glob("[0-9][0-9]_*.ipynb")))))
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=RAIZ, capture_output=True, text=True).stdout.strip() or "local"
    except OSError:
        commit = "local"
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    hoje = dt.date.today()
    subprocess.run(["pandoc", "livro.md", "-f", "markdown+tex_math_dollars+raw_attribute+pipe_tables-implicit_figures-yaml_metadata_block-multiline_tables-simple_tables-grid_tables",
                    "-t", "latex", "--top-level-division=chapter", "--template", str(LIVRO / "modelo.tex"),
                    "--highlight-style=tango", "--lua-filter", str(LIVRO / "equacoes.lua"), "-V", f"data={meses[hoje.month - 1]} de {hoje.year}", "-V", "edicao=1",
                    "-V", f"commit={commit}", "-V", f"verificacoes={verif}", "-o", "livro.tex"], cwd=BUILD, check=True)
    if "--so-tex" in sys.argv:
        return
    subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "livro.tex"], timeout=1500,
                   cwd=BUILD, check=True, stdout=subprocess.DEVNULL)
    shutil.copy(BUILD / "livro.pdf", SAIDA_PDF)
    print("PDF:", SAIDA_PDF, f"({verif} verificações)")


if __name__ == "__main__":
    sys.exit(main())
