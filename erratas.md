# Erratas e notas sobre o livro

Esta página junta, módulo a módulo, as erratas e observações registradas nos notebooks. Cada item foi
conferido numericamente no laboratório correspondente. O livro de referência é *Derivatives Analytics
with Python* (Y. Hilpisch, Wiley, 2015); as seções e equações citadas são as do livro.

Página gerada automaticamente por `scripts/gerar_erratas.py`.

## Módulo 2 — Fatos estilizados e volatilidade implícita

Notebook: [02_fatos_estilizados](02_fatos_estilizados.ipynb)

| Local | Problema |
|---|---|
| Comentário 4 após a saída da GBM | cita p-valor conjunto de 0,426, enquanto a saída impressa mostra 0,374 |
| §3.4.2, contagem de saltos | escreve $P(r_n > -0{,}05)$; deveria ser $+0{,}05$ |
| §3.4.2, contagem de saltos | as probabilidades informadas (2,911 e 3,402 por 10.000 dias) não fecham com $\hat\mu$ e $\hat\sigma$ impressos, que dão 1,267 e 1,542 por 10.000 dias |
| §3.5.2, primeira bolha | diz que calls OTM têm implícita mais alta; a Figura 3.11 mostra isso para calls ITM (puts OTM) |

## Módulo 3 — Neutralidade ao risco em tempo discreto

Notebook: [03_neutralidade_discreto](03_neutralidade_discreto.ipynb)

| Local | Problema |
|---|---|
| Defs. 19 e 25 | admissibilidade com $V_t \ge -\alpha$ torna "arbitragem" qualquer estratégia alavancada com ganho esperado positivo; o correto (Harrison-Pliska) é $V_t \ge 0$ |
| Prova do Lema 1 | "$u < t$" na definição de $\psi$ deveria ser "$u > t$" |
| Prova da Prop. 1 | a soma usa $\beta_{t+1}S_{t+1}$; o correto é $\beta_{t-1}S_{t-1}$ |
| Prova da Prop. 1 | "trading strategy $\zeta \in T$" deveria ser $\phi$ |
| Nota 13 | refere "condição 3 da definição 3"; o certo é definição 1 (álgebra) |

## Módulo 4 — Tempo contínuo: Browniano, Itô e Girsanov

Notebook: [04_tempo_continuo](04_tempo_continuo.ipynb)

| Local | Comentário |
|---|---|
| Justificativa de (4.1) | a esperança da integral é zero só se $V$ for martingale verdadeiro; admissibilidade garante apenas $\mathbb{E}^Q[V_T] \le V_0$ |
| Teorema 3 | a medida é martingale local (sigma-martingale, no caso mais geral), e não martingale, para $S$ não limitado |
| Def. 37 (arbitragem contínua) | exige $V_T \ge 0$, corrigindo a Def. 25 do caso discreto |
| Geral | o teorema de Girsanov não é tratado; o livro passa direto à dinâmica sob $Q$ |

## Módulo 5 — Black-Scholes-Merton: a EDP, a fórmula e as gregas

Notebook: [05_bsm](05_bsm.ipynb)

| Local | Problema |
|---|---|
| Passagem para (5.6) | $r(V - \partial V/\partial S)$ deveria ser $r(V - S\,\partial V/\partial S)$ |
| Equação (5.6) | falta o fator $rS$ no primeiro termo: o correto é $rS\,\partial V/\partial S$ |
| §5.2.2 | a carteira $\Pi = V - \Delta S$ não é autofinanciada; a dedução usa $\Delta$ fixo no intervalo |
| §5.2.3, item 1 | "$K > 100$ for the put, OTM" deveria ser $K < 100$ |

## Módulo 6 — A árvore binomial de Cox-Ross-Rubinstein

Notebook: [06_crr](06_crr.ipynb)

| Local | Comentário |
|---|---|
| Nota da Tabela 5.1 | diz "put"; a tabela é de call |
| §5.4, após a Figura 5.8 | atribui a oscilação a "parametrização diferente"; o motivo é a paridade de $M$ em relação à posição de $K$ |

## Módulo 7 — Fourier I: da função característica à fórmula de Lewis

Notebook: [07_fourier_lewis](07_fourier_lewis.ipynb)

| Local | Comentário |
|---|---|
| Prova da Prop. 6 | a expressão $(z - i/2)^2 - (z - i/2)i = z^2 - 2zi + 1/4$ está errada; o denominador correto, com a reta em $u_i = 1/2$, é $z^2 + 1/4$. A fórmula (6.5) está certa |
| Geral | a existência de $\phi$ em argumentos complexos exige uma faixa de analiticidade, que o texto não discute |

## Módulo 8 — Fourier II: Carr-Madan, FFT e convolução

Notebook: [08_fourier_fft](08_fourier_fft.ipynb)

| Local | Problema |
|---|---|
| §6.5.1 | $e^{iux}$ está expandida incorretamente: o fator é $e^{-u_ix}$ e a oscilação usa apenas $u_r$ |
| Def. 43 | as somas de potências devem começar em $j = 0$ |
| Def. 43 | potências positivas de $z_n$ giram em sentido horário |
| Def. 44 | a inversa da DFT precisa do fator $1/n$ |
| §6.6.2, equação (6.13) | a lei $\ln(1+J) \sim N(\ln(1+\mu_J) - \delta^2/2, \delta^2)$ não é compatível com $r_J = \lambda(e^{\mu_J + \delta^2/2} - 1)$ e com (6.14), que correspondem a $\ln(1+J) \sim N(\mu_J, \delta^2)$ |
| §6.6.3 | o vetor $qv = (0{,}5034;\ 0{,}4966; \dots)$ é incompatível com $q = 0{,}5378$ |
| Equação (6.6) | falta tomar a parte real |
| §6.6.1, precisão da FFT | os cinco dígitos relatados vêm do ramo OTM do script, de cauda lenta; não são um limite da FFT |

## Módulo 9 — Opções americanas por simulação: LSM e dual

Notebook: [09_americanas_lsm](09_americanas_lsm.ipynb)

| Local | Comentário |
|---|---|
| Tabelas 7.1 e 7.2 | a referência (árvore de 500 passos) é americana; os algoritmos estimam bermudanas de $M$ datas. Boa parte da "diferença" reportada, sobretudo no condor, é a diferença entre as duas |
| Tabela 7.2, nota | diz "American put option"; a tabela é do short condor |
| Tabela 7.1 e §7.4.1 | o espaçamento entre LSM e dual é atribuído ao algoritmo; ele vem sobretudo do ruído da simulação aninhada ($J = 50$), que infla o limite superior |
| Equações (7.8) a (7.12) | o martingale deve ser expresso em unidades descontadas, como $h$; o texto mistura $B_0(t)[h_t - \mathcal{M}_t]$ com um $\mathcal{M}^*$ formado por valores não descontados |
| Equação (7.11) | o máximo passa de $t \in \{\Delta t, \dots, T\}$ para $t \in \{0, \dots, T\}$ sem comentário |

## Módulo 10 — Primeiro exemplo completo: avaliação baseada em mercado com Merton

Notebook: [10_merton_mercado](10_merton_mercado.ipynb)

| Local | Comentário |
|---|---|
| §8.2 | a lei $\ln(1+J) \sim N(\ln(1+\mu_J) - \delta^2/2, \delta^2)$ não é a usada em $r_J$, em (8.2) e nos scripts, que correspondem a $\ln(1+J) \sim N(\mu_J, \delta^2)$ |
| §8.5, saída do script | os valores "Int" usam integração até $z = 50$, curta demais para $T = 0{,}22$; são os valores FFT que estão corretos |
| Equações (8.5) e (8.6) | o salto é somado, e $y$ saltos no mesmo passo usam um único tamanho multiplicado por $y$; o esquema tem viés |
| §8.5, saída do script | a diferença entre simulação e fórmula combina esse viés com ruído de uma única semente |
| Script 8.7.5 | comenta "T = 0.22 # shortest maturity", mas o prazo mais curto é de 17 dias (0,047 ano) |

## Módulo 11 — O modelo geral BCC97: volatilidade estocástica, saltos e juros estocásticos

Notebook: [11_bcc97](11_bcc97.ipynb)

| Local | Comentário |
|---|---|
| §9.2 | a lei do salto não corresponde a $r_J$ nem a (9.11); o correto é $J \sim N(\mu_J, \delta^2)$ para o log-salto |
| Eq. (9.8) | $\partial^2C/\partial S$ deveria ser $\partial^2C/\partial S^2$ |
| Eq. (9.8) | faltam os fatores $v$ e $r$ nos termos $\tfrac12\sigma_v^2\,\partial^2C/\partial v^2$ e $\tfrac12\sigma_r^2\,\partial^2C/\partial r^2$ |
| Prova da Prop. 8 | o salto entra como $\partial A/\partial S\cdot jdN$, aproximação de primeira ordem; o certo é a diferença exata, como a própria (9.8) usa |
| Prova da Prop. 8 | na primeira linha da expansão, $\partial A/\partial t$ aparece dentro do fator $\tfrac12$ |
| §9.5.2 | o uso de $r_{0,T} = -\ln B_0(T)/T$ é uma aproximação, não o tratamento de juros estocásticos do artigo original |
| Eq. (9.10) | a forma usada é a estável, com $c_2 = -d$; ponto positivo do livro |

## Módulo 12 — Monte Carlo: discretização e redução de variância

Notebook: [12_monte_carlo](12_monte_carlo.ipynb)

| Onde | O quê |
|---|---|
| §10.6.3 e §10.6.4, processo do índice | usa `v[t]` (fim do passo) em vez de `v[t-1]`; cria o drift espúrio $\tfrac12\rho\sigma_v$ por unidade de tempo em $\ln S$, que não diminui com $\Delta t$ |
| Tabela 10.1 e Figura 10.4 | o salto de precisão atribuído ao casamento de momentos é, em sua maior parte, a correção de drift (`bias`) desfazendo o problema acima; com `v[t-1]` não há salto |
| §10.3, lista de esquemas | "Truncation" coincide com "Absorption" e "Simple Reflection" com "Reflection": são cinco esquemas, não sete |
| §10.2, Figuras 10.2 e 10.3 | a referência em $t > 0$ é $P(\mathbb{E}[r_t])$, mas a média de Monte Carlo estima $\mathbb{E}[P(r_t)]$; a diferença (Jensen) é da ordem do viés do Euler que se quer mostrar |
| §10.6.2, esquema exato | `np.ramdom.chisquare` (erro de digitação) |
| §10.6.4, correlação | $\rho$ posto entre juros e índice, e não entre variância e índice; o controle europeu disfarça o efeito |
| §10.4, controle | a média do controle usa Heston com taxa constante $\bar r$, uma aproximação (Módulo 11), pequena para prazos de até seis meses |
| §10.2 | a transição por qui-quadrado não central é clássica (Feller, 1951; Cox, Ingersoll e Ross, 1985); Broadie e Kaya (2006) a usam na simulação exata do Heston |
| Scripts | Python 2 (`xrange`, `print` sem parênteses; `I / 2` vira real no Python 3) |

## Módulo 13 — Calibração I: a curva de juros no CIR e as opções no Heston

Notebook: [13_calibracao_cir_heston](13_calibracao_cir_heston.ipynb)

| Onde | O quê |
|---|---|
| Exemplo 4 (§11.2.1) | o limite é $\nu < 1/2$, não $1/4$; o intervalo de preços é $]4, 8[$, e não $]4, 9[$; e em $\nu = 1/4$ o preço seria 6, não "$1 + 8 = 9$" |
| Eq. (11.6) e código da §11.6.1 | falta o fator 2 no primeiro termo: o correto é $2\kappa_r\theta_r(e^{\gamma t} - 1)/D$; o $\theta_r$ calibrado sai dobrado |
| §11.6.1, ponto de partida | com a fórmula do livro, o Nelder-Mead a partir de $(1;\ 0{,}02;\ 0{,}1)$ pode parar longe do ajuste |
| §11.3.2, dados | a Eonia de 01/10/2014 ($-0{,}032\%$) é usada como $r_0$ do CIR, que não admite taxas negativas |
| §11.3.2, contagem | o texto chama a Euribor de "30/360", mas o código usa dias corridos/360 (real/360, que é a convenção da Euribor); os prazos das opções usam /365 |
| Eq. (11.7) | $B_t(T) = a\,e^{-b\,\mathbb{E}[r_t]}$ não é o preço esperado do título em $t$ (desigualdade de Jensen; ver Módulo 12) |
| §11.4.1, $H_1$ | o logaritmo impresso traz $1 - c_1e^{c_3T}$; o correto (e o código) é $1 - c_3e^{c_2T}$ |
| §11.4.3 | a solução ($\kappa_v = 18{,}447$) está na fronteira de Feller: a restrição está ativa |
| §11.6.2 | `options.ix` foi removido do pandas; use `.loc` |

## Módulo 14 — Calibração II: saltos, regularização e o BCC97 completo

Notebook: [14_calibracao_bcc97](14_calibracao_bcc97.ipynb)

| Onde | O quê |
|---|---|
| §11.6.4, `BCC_calibration_short` | `opt1` e `local_opt` são atribuídos sem `global`: viram variáveis locais, e a penalidade da função objetivo nunca é aplicada |
| Eq. (11.17) | a penalidade é a norma $\lVert p - p_0\rVert$, não o quadrado: não é Tikhonov; com $w = 1$ e EQM em pontos², congela os parâmetros no ponto de partida |
| §11.4.4, resultados | $\lambda = 0{,}008$, $\mu_J = -0{,}600$ (no limite) e $\delta = 0{,}001$: na prática, nenhum salto; sintoma da calibração sequencial |
| §11.4.5, resultados | $\rho = -0{,}999$ e $\delta = 0{,}000$ na fronteira, $\lambda = 0{,}008$: o BCC97 calibrado é praticamente um Heston |
| §11.4.6, resultados | $\kappa_v$ vai de 22,2 a 28,5 entre (11.1) e (11.4), funções quase iguais: parâmetros mal identificados; $\mu_J = -0{,}600$ de novo no limite |
| §11.6.5 e §11.6.6 | a condição de Feller continua imposta (ver Módulo 13) |
| §11.6.2 e seguintes | Nelder-Mead com restrições por "valor alto" pode parar cedo encostado numa parede; sem reinício, o resultado depende de detalhes mínimos dos dados |
| §11.6.6 | `options.ix` foi removido do pandas; use `.loc` |

## Módulo 15 — Simulação e avaliação no modelo geral BCC97

Notebook: [15_simulacao_bcc97](15_simulacao_bcc97.ipynb)

| Onde | O quê |
|---|---|
| §12.5.1, `B96_generate_paths` | `rj` é calculado e nunca usado: falta o compensador $-r_J\Delta t$ de (12.1); o índice perde $\lvert r_J\rvert$ de drift por ano |
| Eq. (12.1) e código | saltos aditivos com um único tamanho para todos os $y_t$ saltos do passo; o exato é $e^{N\mu_J + \sqrt N\delta z}$ |
| Eq. (12.1) e código | a variância do passo é `v[t]`, do fim do passo (Módulo 12); com $\rho = -0{,}999$, o drift espúrio é $-0{,}475$ por ano |
| §12.3.1 | o viés de 22 a 52 pontos atribuído ao número de passos vem do `v[t]`; o esquema exato acerta com 50 passos por ano a partir de 6 meses (só no prazo de 1 mês, com 4 passos, há viés de Euler de 1 a 2 pontos) |
| §12.3.2 | a "diferença" americana − europeia mistura prêmio e viés de simulação |
| §12.5.3, título | "American Call Options", mas o script avalia puts |
| Parâmetros do livro | $\rho = -0{,}999$, $\delta = 0$ e $\lambda = 0{,}008$ vêm da calibração degenerada do Módulo 14 |
| Scripts | Python 2 (`xrange`, `print`, `I / 2`) |

## Módulo 16 — Hedge dinâmico e síntese

Notebook: [16_hedge_dinamico](16_hedge_dinamico.ipynb)

| Onde | O quê |
|---|---|
| §13.5.1 e §13.5.3, delta inicial | os dois preços LSM da diferença finita usam números aleatórios diferentes: o delta inicial é dominado pelo ruído (desvio-padrão acima de 0,5) |
| §13.5.1, regra de exercício | `h >= C` com `C` truncado em zero marca como exercidas puts fora do dinheiro, encerrando o hedge antes da hora |
| §13.5.2 | P&L calculado nas mesmas trajetórias da regressão (dentro da amostra), apesar de a nota 3 defender a avaliação fora da amostra |
| §13.3, P&L médio de +4,34 | numa simulação sob $Q$, o P&L médio de um hedge autofinanciável iniciado no preço justo é zero; o valor positivo vem do simulador (Módulo 15) |
| §13.3, "risco de salto diversificável" | a hipótese de Merton é de diversificação entre ativos; não vale para muitas opções sobre o mesmo índice, cujos saltos são comuns |
| §13.5.3 | herda o simulador do cap. 12 (`v[t]`, compensador ausente, saltos aditivos, casamento de momentos) |
| Cap. 14 | o resumo é fiel ao livro; os módulos 12 a 16 mostram que as etapas de simulação, calibração e hedge precisam das conferências da Seção 6.2 |
