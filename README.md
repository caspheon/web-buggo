# Buggo — deck de apresentação

Versão web do `buggo_pitch.pptx` (15 slides), feita para apresentar sem depender
do PowerPoint. No slide 11 o celular mostra a gravação do app rodando, que
começa sozinha e sem som ao chegar no slide.

Cada slide monta o conteúdo em ordem quando entra em cena: a frase sobe e o
grito (`FECHAR!`, `DESISTI!`) entra depois, com pausa; os números do mercado
sobem contando e as barras do gráfico crescem; a linha que liga o celular ao texto se
desenha. Quem tiver "reduzir movimento" ligado no sistema vê tudo estático.

## Como apresentar

1. Abra `index.html` no navegador (duplo clique).
2. Pressione **F** para tela cheia.
3. Avance com **→** / **espaço** ou clicando na tela.

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
| `T` | cronômetro (`R` zera) |
| `?` | lista de atalhos |
| `Esc` | fecha o que estiver aberto |

A URL guarda o slide atual (`index.html#7`), então recarregar a página não perde
o lugar.

## Plano B

- **PDF**: `Ctrl+P` → Salvar como PDF, retrato desligado. Sai um slide por página.
- **Link**: a mesma apresentação está publicada como Artifact, para abrir de
  qualquer computador.

## Estrutura

- `index.html` — a apresentação inteira (HTML + CSS + JS em um arquivo só)
- `assets/` — imagens extraídas do `.pptx` e `buggo-app.mp4`, a gravação do app
- `build-artifact.py` — gera `dist/buggo-pitch.html`, a versão de arquivo único
  com as imagens e o vídeo embutidos, usada na publicação
