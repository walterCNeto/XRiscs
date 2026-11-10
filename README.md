# XRiscs — Derivativos com Python

Curso em português, em 16 notebooks, sobre avaliação baseada em mercado de opções sobre índices, construído sobre o livro *Derivatives Analytics with Python* (Y. Hilpisch, Wiley, 2015): teoria passo a passo, laboratórios em Python e 435 verificações numéricas automáticas.

**Leia online:** https://waltercneto.github.io/XRiscs

## Conteúdo

| # | Módulo | Livro |
|---|---|---|
| 01 | O que é avaliação baseada em mercado | caps. 1-2 |
| 02 | Fatos estilizados e volatilidade implícita | cap. 3 |
| 03 | Neutralidade ao risco em tempo discreto | cap. 4 |
| 04 | Tempo contínuo: Browniano, Itô e Girsanov | cap. 4 |
| 05 | Black-Scholes-Merton | cap. 5 |
| 06 | Árvore binomial CRR | cap. 5 |
| 07 | Fourier I: Lewis | cap. 6 |
| 08 | Fourier II: Carr-Madan e FFT | cap. 6 |
| 09 | Americanas: LSM e dual | cap. 7 |
| 10 | Merton e o mercado | cap. 8 |
| 11 | O modelo geral BCC97 | cap. 9 |
| 12 | Monte Carlo: discretização e redução de variância | cap. 10 |
| 13 | Calibração I: CIR e Heston | cap. 11 |
| 14 | Calibração II: saltos e BCC97 | cap. 11 |
| 15 | Simulação no BCC97 | cap. 12 |
| 16 | Hedge dinâmico e síntese | caps. 13-14 |

A página `erratas.md` (gerada por `scripts/gerar_erratas.py`) reúne as correções ao livro encontradas nos laboratórios.

## Rodar localmente

```bash
conda env create -f environment.yml
conda activate xriscs
jupyter lab                  # estudar
pytest -q                    # executar todos os notebooks e conferir as verificações (~15 min)
jupyter-book build .         # gerar o site em _build/html
```

## Publicação

A cada push na `main`, o workflow `publicar-livro` gera o site com Jupyter Book (notebooks já executados) e publica na branch `gh-pages`. Os testes completos rodam no workflow `testes-notebooks` (manual, semanal e em pull requests).

## Licença

Código: MIT. Textos: CC BY 4.0. Material de estudo independente, sem afiliação com o autor ou a editora do livro; o livro não faz parte do repositório.

Walter C. Neto — https://waltercneto.github.io
