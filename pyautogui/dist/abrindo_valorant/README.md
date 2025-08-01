# 🎮 Auto-Valorant Launcher

Bem-vindo ao **Auto-Valorant Launcher**!  
Esse é um projetinho simples feito em Python com `pyautogui` que automatiza o processo de abrir o Valorant e entrar direto num mata-mata 🧠💥.  
Foi feito especialmente para minha máquina, então os cliques estão posicionados com base no meu monitor e setup.

---

## 🚀 O que esse projeto faz?

A ideia é:  
Você abre o `.exe`, vai pegar uma água, um lanche 🥤🍪... e quando volta, o Valorant já está aberto, no **mata-mata**, pronto pra aquecer!  
Sem precisar clicar em nada, sem enrolação.

---

## 🛠 Como funciona?

O programa simula os cliques que **eu mesmo faria**, na seguinte ordem:

1. 🖱 Abre o **Client da Riot** (clicando onde ele está fixado no meu monitor).
2. ⌛ Espera o carregamento.
3. 🖱 Clica no **Valorant** dentro do Client.
4. ⌛ Espera o jogo abrir.
5. 🖱 Clica em **Jogar**, seleciona o **Mata-Mata (Deathmatch)** e clica em **Encontrar Partida**.

Tudo isso com delays e coordenadas pensados exatamente para o meu PC.




---

## ⚠️ Observações

> ⚠️ **IMPORTANTE**:  
Esse projeto foi feito 100% com base nas **posições dos botões na minha tela**.  
Ou seja, se você baixar esse projeto, **ele provavelmente não vai funcionar direto no seu PC**, a menos que você:
- Tenha a **mesma resolução de tela**,
- E os **atalhos fixados nos mesmos lugares que eu**.

Caso queira adaptar, você pode usar o próprio `pyautogui.position()` no terminal pra descobrir as coordenadas dos seus cliques e editar o código.

---
## 📦 Instalação das dependências

Antes de usar o script, instale as bibliotecas necessárias com o comando abaixo:

```bash
pip install pyautogui pyinstaller


## 📦 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/auto-valorant-launcher.git
