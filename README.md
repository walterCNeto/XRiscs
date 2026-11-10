# XRiscs — Derivativos com Python

Curso em português, em 20 notebooks, sobre precificação calibrada ao mercado de opções sobre índices, construído sobre o livro *Derivatives Analytics with Python* (Y. Hilpisch, Wiley, 2015): teoria passo a passo, laboratórios em Python e 530 verificações numéricas automáticas. Os módulos 17 a 19 complementam o livro com modelos de juros: Hull-White (fórmulas fechadas e árvore trinomial) e a simulação calibrada de trajetórias, do Vasicek ao HJM. O módulo 20 traz as árvores implícitas de Derman-Kani-Chriss, com um widget interativo para construir e desenhar a árvore.

**Leia online:** https://waltercneto.github.io/XRiscs

## Conteúdo

| # | Módulo | Livro |
|---|---|---|
| 01 | Mercados, arbitragem e precificação de derivativos | caps. 1-2 |
| 02 | Stylized facts e volatilidade implícita | cap. 3 |
| 03 | A medida neutra ao risco em tempo discreto | cap. 4 |
| 04 | Cálculo estocástico: browniano, Itô e Girsanov | cap. 4 |
| 05 | Black-Scholes-Merton | cap. 5 |
| 06 | Árvore binomial CRR | cap. 5 |
| 07 | Métodos de Fourier I: Lewis | cap. 6 |
| 08 | Métodos de Fourier II: Carr-Madan e FFT | cap. 6 |
| 09 | Americanas: Longstaff-Schwartz e dual | cap. 7 |
| 10 | Calibração ao mercado com Merton | cap. 8 |
| 11 | O modelo BCC97 | cap. 9 |
| 12 | Monte Carlo: discretização e redução de variância | cap. 10 |
| 13 | Calibração I: CIR e Heston | cap. 11 |
| 14 | Calibração II: saltos e BCC97 | cap. 11 |
| 15 | Simulação e precificação no BCC97 | cap. 12 |
| 16 | Hedge dinâmico e síntese | caps. 13-14 |
| 17 | Hull-White I: medidas, modelo e fórmulas fechadas | complemento |
| 18 | Hull-White II: árvore trinomial e Black-Karasinski | complemento |
| 19 | Simulação de trajetórias de juros: do Vasicek ao HJM | complemento |
| 20 | Árvores implícitas de Derman-Kani-Chriss (interativo) | complemento |

A página `erratas.md` (gerada por `scripts/gerar_erratas.py`) reúne as correções ao livro encontradas nos laboratórios.

## Rodar localmente

```bash
conda env create -f environment.yml
conda activate xriscs
jupyter lab                  # estudar
pytest -q                    # executar todos os notebooks e conferir as verificações (~17 min)
jupyter-book build .         # gerar o site em _build/html
```

## Publicação

A cada push na `main`, o workflow `publicar-livro` gera o site com Jupyter Book (notebooks já executados) e publica na branch `gh-pages`. Os testes completos rodam no workflow `testes-notebooks` (manual, semanal e em pull requests).

## Licença

Código: MIT. Textos: CC BY 4.0. Material de estudo independente, sem afiliação com o autor ou a editora do livro; o livro não faz parte do repositório.

Walter C. Neto — https://waltercneto.github.io
