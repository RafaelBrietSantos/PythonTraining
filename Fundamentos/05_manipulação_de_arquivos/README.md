<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="100"/>
</p>

# 💾 Guarde e Recupere: Manipulação de Arquivos em Python! 📂
## 05_Manipulacao_de_Arquivos ✍️

**Chegou a hora de dar persistência aos seus dados!** ✨

Nesta pasta, você aprenderá uma habilidade essencial em programação: a **Manipulação de Arquivos**. Isso significa que seus programas não serão mais "esquecidos" após serem fechados. Aqui, você dominará como ler e escrever informações em arquivos de texto, permitindo que seus dados sejam salvos e acessados a qualquer momento.

Você verá como criar, abrir, adicionar conteúdo e ler arquivos, transformando seus programas em ferramentas mais robustas e capazes de interagir com o sistema de arquivos do computador. Cada script é um passo para você controlar o fluxo de dados dos seus projetos!

---

### Conteúdo dos Arquivos:

* [`1_aprendendo_manipular_arquivos.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/05_Manipulacao_de_Arquivos/1_aprendendo_manipular_arquivos.py) 📝
    * **Problema:** Desenvolver um programa que permita ao usuário criar um arquivo de texto com um nome personalizado e escrever conteúdo dentro dele, garantindo que o nome do arquivo seja dinamicamente gerado (ex: 'meu_documento.txt').
    * **Propósito:** Introduzir os conceitos fundamentais de criação, escrita e fechamento de arquivos em Python.
    * **Conceitos Chave:** `input()`, `open()` com modo 'w' (write), `write()`, `close()`, e formatação dinâmica de nomes de arquivo (`.format()` ou f-strings).

* [`2_analise_renda_e_arquivo.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/05_Manipulacao_de_Arquivos/2_analise_renda_e_arquivo.py) 📊
    * **Problema:** Criar um programa que colete informações sobre a renda familiar (número de pessoas, renda de quem trabalha) e calcule a renda per capita. Em seguida, o programa deve salvar todos esses dados em um novo arquivo de texto e, por fim, ler e exibir o conteúdo desse arquivo.
    * **Propósito:** Desafiar a combinação de entrada de dados, lógica condicional (`if/else` aninhados) e operações básicas de manipulação de arquivos (criação e escrita com modo 'x', e leitura com modo 'r').
    * **Conceitos Chave:** `input()`, `strip()`, `title()`, `int()`, `float()`, `if`/`else` para diferentes cenários de entrada, cálculo de renda per capita, `open()` com modos 'x' (criação exclusiva) e 'r' (leitura), `write()`, `read()`, `close()`, e f-strings para formatação de texto e nomes de arquivo.
    * **Atenção:** Este código espera que as entradas numéricas sejam válidas. Se um texto for digitado onde se espera um número, ou se o número de pessoas for zero, ou se o arquivo já existir no modo 'x', o programa pode gerar erros.
