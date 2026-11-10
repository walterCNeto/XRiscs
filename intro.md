# XRiscs — Derivativos com Python

**Avaliação baseada em mercado de opções sobre índices: da teoria à calibração e ao hedge, em 16 laboratórios.**

Este é um curso de estudo, em português, construído sobre o livro *Derivatives Analytics with Python* (Yves Hilpisch, Wiley, 2015). Ele segue a sequência do livro, do modelo de Black-Scholes-Merton até o modelo geral de Bakshi, Cao e Chen (volatilidade estocástica, saltos e juros estocásticos), e acrescenta a cada passo o que o livro deixa implícito: as deduções completas e um laboratório em Python que confere cada resultado numericamente.

## Como o curso é organizado

Cada módulo é um notebook com a mesma estrutura:

1. **Objetivos** e a ligação com os módulos anteriores.
2. **Teoria passo a passo**, com as deduções escritas por inteiro.
3. **Laboratórios** em Python: cada afirmação importante é conferida por código, com verificações automáticas (`ok(...)`) que interrompem o notebook se a conta não fechar. São **435 verificações** no curso.
4. **Síntese**, **erratas e notas** sobre o trecho do livro, e **exercícios** com solução.

Todos os dados são **sintéticos**. Isso permite algo que dados reais não permitem: calibrar um modelo onde a resposta é conhecida e ver o que a calibração recupera e o que ela não consegue identificar.

## Mapa dos módulos

| Módulo | Tema | Livro |
|---|---|---|
| [1](01_avaliacao_baseada_em_mercado) | O que é avaliação baseada em mercado | caps. 1-2 |
| [2](02_fatos_estilizados) | Fatos estilizados e volatilidade implícita | cap. 3 |
| [3](03_neutralidade_discreto) | Neutralidade ao risco em tempo discreto | cap. 4 |
| [4](04_tempo_continuo) | Tempo contínuo: Browniano, Itô e Girsanov | cap. 4 |
| [5](05_bsm) | Black-Scholes-Merton: a EDP, a fórmula e as gregas | cap. 5 |
| [6](06_crr) | A árvore binomial de Cox-Ross-Rubinstein | cap. 5 |
| [7](07_fourier_lewis) | Fourier I: da função característica à fórmula de Lewis | cap. 6 |
| [8](08_fourier_fft) | Fourier II: Carr-Madan, FFT e convolução | cap. 6 |
| [9](09_americanas_lsm) | Opções americanas por simulação: LSM e dual | cap. 7 |
| [10](10_merton_mercado) | Primeiro exemplo completo: Merton e o mercado | cap. 8 |
| [11](11_bcc97) | O modelo geral BCC97 | cap. 9 |
| [12](12_monte_carlo) | Monte Carlo: discretização e redução de variância | cap. 10 |
| [13](13_calibracao_cir_heston) | Calibração I: a curva de juros no CIR e as opções no Heston | cap. 11 |
| [14](14_calibracao_bcc97) | Calibração II: saltos, regularização e o BCC97 completo | cap. 11 |
| [15](15_simulacao_bcc97) | Simulação e avaliação no modelo geral | cap. 12 |
| [16](16_hedge_dinamico) | Hedge dinâmico e síntese | caps. 13-14 |

A página [Erratas e notas](erratas) reúne, módulo a módulo, as correções ao livro encontradas nos laboratórios: de sinais e fatores em fórmulas a detalhes dos scripts que mudam os resultados numéricos.

## Pré-requisitos

* Cálculo e probabilidade no nível de um primeiro curso de graduação.
* Python com NumPy, pandas e matplotlib no nível básico.
* Não é preciso conhecer derivativos: o Módulo 1 começa do zero, e o cálculo estocástico é construído nos Módulos 3 e 4.

## Como usar

**No navegador.** Cada página tem um botão de foguete (no topo) para abrir o notebook no Google Colab ou no Binder e executá-lo.

**No seu computador.**

```bash
git clone https://github.com/walterCNeto/XRiscs.git
cd XRiscs
conda env create -f environment.yml
conda activate xriscs
jupyter lab
```

Os notebooks estão salvos já executados. Para conferir que todos rodam e passam nas verificações: `pytest -q` (cerca de 15 minutos).

## Convenções

* Números em tabelas e saídas com **três casas decimais**, no padrão brasileiro (vírgula decimal).
* Referências como "§11.4.3" ou "(10.6)" são seções e equações do livro.
* Sementes aleatórias fixas: os resultados são reproduzíveis.

## Licença e créditos

Código sob licença MIT; textos sob CC BY 4.0. Este é um material de estudo independente: não reproduz o livro, não substitui sua leitura e não tem afiliação com o autor ou a editora. O livro está em [Wiley](https://www.wiley.com/) e o site oficial do autor é [derivatives-analytics-with-python.com](http://derivatives-analytics-with-python.com).

Autor: **Walter C. Neto** — [waltercneto.github.io](https://waltercneto.github.io)
