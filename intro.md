# XRiscs — Derivativos com Python

**Precificação de derivativos em Python: opções sobre índices, da teoria à calibração ao mercado e ao hedge, com complementos sobre modelos de juros e árvores implícitas. São 20 módulos com laboratórios.**

Este é um curso de estudo, em português, construído sobre o livro *Derivatives Analytics with Python* (Yves Hilpisch, Wiley, 2015). Ele segue a sequência do livro, do modelo de Black-Scholes-Merton até o modelo geral de Bakshi, Cao e Chen (volatilidade estocástica, saltos e juros estocásticos), e acrescenta a cada passo o que o livro deixa implícito: as deduções completas e um laboratório em Python que confere cada resultado numericamente.

```{admonition} O curso em livro
:class: tip
Os 20 módulos também estão reunidos num livro em PDF, com sumário, código, saídas e figuras de todos os laboratórios: {download}`baixe o livro (PDF) <livro/XRiscs_Derivativos_com_Python.pdf>`.
```

## Como o curso é organizado

Cada módulo é um notebook com a mesma estrutura:

1. **Objetivos** e a ligação com os módulos anteriores.
2. **Teoria passo a passo**, com as deduções escritas por inteiro.
3. **Laboratórios** em Python: cada afirmação importante é conferida por código, com verificações automáticas (`ok(...)`) que interrompem o notebook se a conta não fechar. São **530 verificações** no curso.
4. **Síntese**, **erratas e notas** sobre o trecho do livro, e **exercícios** com solução.

Todos os dados são **sintéticos**. Isso permite algo que dados reais não permitem: calibrar um modelo onde a resposta é conhecida e ver o que a calibração recupera e o que ela não consegue identificar.

## Mapa dos módulos

| Módulo | Tema | Livro |
|---|---|---|
| [1](01_avaliacao_baseada_em_mercado) | Mercados, arbitragem e precificação de derivativos | caps. 1-2 |
| [2](02_fatos_estilizados) | Stylized facts e volatilidade implícita | cap. 3 |
| [3](03_neutralidade_discreto) | A medida neutra ao risco em tempo discreto | cap. 4 |
| [4](04_tempo_continuo) | Cálculo estocástico: movimento browniano, Itô e Girsanov | cap. 4 |
| [5](05_bsm) | Black-Scholes-Merton: a EDP, a fórmula e as gregas | cap. 5 |
| [6](06_crr) | A árvore binomial de Cox-Ross-Rubinstein | cap. 5 |
| [7](07_fourier_lewis) | Métodos de Fourier I: da função característica à fórmula de Lewis | cap. 6 |
| [8](08_fourier_fft) | Métodos de Fourier II: Carr-Madan, FFT e convolução | cap. 6 |
| [9](09_americanas_lsm) | Opções americanas por simulação: Longstaff-Schwartz e o problema dual | cap. 7 |
| [10](10_merton_mercado) | Calibração ao mercado com o modelo de saltos de Merton | cap. 8 |
| [11](11_bcc97) | O modelo BCC97: volatilidade estocástica, saltos e juros estocásticos | cap. 9 |
| [12](12_monte_carlo) | Monte Carlo: discretização e redução de variância | cap. 10 |
| [13](13_calibracao_cir_heston) | Calibração I: a curva de juros no CIR e as opções no Heston | cap. 11 |
| [14](14_calibracao_bcc97) | Calibração II: saltos, regularização e o BCC97 completo | cap. 11 |
| [15](15_simulacao_bcc97) | Simulação e precificação no modelo BCC97 | cap. 12 |
| [16](16_hedge_dinamico) | Hedge dinâmico e síntese do curso | caps. 13-14 |
| [17](17_hull_white_teoria) | Hull-White I: medidas, o modelo e as fórmulas fechadas | complemento |
| [18](18_hull_white_arvore) | Hull-White II: a árvore trinomial (e Black-Karasinski) | complemento |
| [19](19_simulacao_juros) | Simulação de trajetórias de juros: do Vasicek ao HJM | complemento |
| [20](20_arvores_implicitas) | Árvores implícitas de Derman-Kani-Chriss, com widget interativo | complemento |

Os Módulos 17 a 19 complementam o livro com modelos de juros. Os dois primeiros tratam do Hull-White, a partir de Wilmott, Clewlow e Strickland e Hull e White: troca de numerário, fórmulas fechadas, caps, estimação de parâmetros e a árvore trinomial com títulos callable e puttable; o Módulo 19 simula e calibra à mesma curva e ao mesmo caplet uma escada de modelos (Vasicek, Ho-Lee, Hull-White, CIR++, Black-Karasinski, G2++ e HJM com componentes principais) e compara o que a calibração não fixa. O Módulo 20 volta às ações: constrói a árvore trinomial implícita de Derman, Kani e Chriss (1996), que reproduz o smile de volatilidade nó a nó, e traz um widget interativo, que roda na própria página, para montar e desenhar a árvore com passos desiguais, nós que acompanham o forward e overrides. O Laboratório 6 do Módulo 17 usa as taxas diárias dos T-bills americanos de 2023 (U.S. Treasury, domínio público), em `dados/`.

A página [Erratas e notas](erratas) reúne, módulo a módulo, as correções ao livro encontradas nos laboratórios: de sinais e fatores em fórmulas a detalhes dos scripts que mudam os resultados numéricos.

## Termos em inglês

Alguns termos ficam em inglês porque é assim que o mercado e a literatura os usam, e a tradução atrapalharia mais do que ajudaria: *smile* e *skew* (de volatilidade), *stylized facts*, *payoff*, *strike*, *hedge*, *forward* (taxa, preço, curva e medida *forward*), *spot*, *short rate*, *moment matching*, *override*. Termos com tradução consagrada em português continuam em português: volatilidade implícita e local, gregas, movimento browniano, medida neutra ao risco, numerário.

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
