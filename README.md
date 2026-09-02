# Buggo — deck de apresentação

Versão web do `buggo_pitch.pptx` (17 slides — os 16 do arquivo original mais o
slide 2, que apresenta o Felipe), feita para apresentar sem depender do
PowerPoint. A capa não abre o deck: ela entra no slide 11, como virada, depois
que a história do Felipe termina em "por que não?". No slide 13 o celular mostra
a gravação do app rodando, que começa sozinha e sem som ao chegar no slide.

Cada slide monta o conteúdo em ordem quando entra em cena: a frase sobe e o
grito (`FECHAR!`, `DESISTI!`) entra depois, com pausa; os números do mercado
sobem contando e as barras do gráfico crescem; a linha que liga o celular ao texto se
desenha. Quem tiver "reduzir movimento" ligado no sistema vê tudo estático — a
tecla `A` ignora essa preferência e liga o movimento de volta.

## Como apresentar

1. Abra `index.html` no navegador (duplo clique).
2. Pressione **F** para tela cheia.
3. A tela fica **preta** — é o slide de abertura. Deixe assim enquanto
   apresenta o projetor e se posiciona.
4. Avance com **→** / **espaço** ou clicando na tela: a história do Felipe
   entra animada. A capa do Buggo só aparece no slide 11.

Roda offline, vídeo incluso. A única coisa que precisa de internet são as fontes
(Poppins e Roboto — sem elas o navegador usa uma fonte parecida).

## Atalhos

| Tecla | Ação |
|---|---|
| `→` `espaço` `PgDn` | próximo slide |
| `←` `PgUp` | slide anterior |
| `Home` / `End` | primeiro / último |
| `F` | tela cheia |
| `G` | ver todos os slides |
| `B` | apagar a tela (fica preta) |
| `M` | liga/desliga o som do vídeo |
| `A` | liga/desliga as animações |
| `T` | cronômetro (`R` zera) |
| `?` | lista de atalhos |
| `Esc` | fecha o que estiver aberto |

A URL guarda o slide atual (`index.html#7`), então recarregar a página não perde
o lugar.

## Se as animações não rodarem

Computador antigo — o do laboratório da faculdade, por exemplo — costuma vir
com as animações do sistema desligadas por desempenho ("Ajustar para melhor
desempenho" no Windows, "Reduzir movimento" no macOS). O navegador repassa isso
para a página e o deck entra estático de propósito.

Aperte **A** (ou clique no raio na barra de baixo) para ligar o movimento assim
mesmo. A escolha fica guardada naquele computador, então basta uma vez. E se a
máquina simplesmente não der conta das animações, o deck percebe sozinho depois
de alguns segundos e volta ao conteúdo fixo, sem deixar slide vazio.

## Plano B

- **PDF**: `Ctrl+P` → Salvar como PDF, retrato desligado. Sai um slide por página.
- **Link**: a mesma apresentação está publicada como Artifact, para abrir de
  qualquer computador.

## Estrutura

- `index.html` — a apresentação inteira (HTML + CSS + JS em um arquivo só)
- `assets/` — imagens extraídas do `.pptx` e `buggo-app.mp4`, a gravação do app
- `build-artifact.py` — gera `dist/buggo-pitch.html`, a versão de arquivo único
  com as imagens e o vídeo embutidos, usada na publicação
