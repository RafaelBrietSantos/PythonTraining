# Variaveis e Tipos de Dados 📚

Esta pasta é dedicada aos **fundamentos iniciais da programação em Python**, focando nos conceitos de **variáveis** 📦, nos **tipos de dados primitivos** (como texto 📝, números inteiros e decimais 🔢, e booleanos ✅) e nas operações básicas de **entrada e saída de informações** ↔️.

Cada arquivo aqui demonstra uma aplicação prática desses conceitos, desde a simples exibição de dados até a manipulação de strings e a identificação de tipos.

---

### Conteúdo dos Arquivos:

* **`01_analisador_de_tipos.py`** 🔍
    * **Propósito:** Pede uma entrada ao usuário e analisa o **tipo de dado** que foi digitado, além de verificar algumas de suas propriedades.
    * **Conceitos Chave:** `input()`, `type()`, e métodos de string como `isspace()`, `isnumeric()`, `isalpha()`, `isalnum()`.

* **`02_saudacao_personalizada.py`** 👋
    * **Propósito:** Solicita o nome do usuário e exibe uma mensagem de boas-vindas customizada.
    * **Conceitos Chave:** `input()`, `print()`, uso de **variáveis** para armazenar dados e **formatação de strings** (`.format()`).

* **`03_analisador_de_string_completo.py`** 🔬
    * **Propósito:** Recebe uma string do usuário e realiza uma análise detalhada, informando diversas características dessa string.
    * **Conceitos Chave:** `input()`, `print()` (com ênfase em **f-strings**), e uma variedade de métodos de string como `isalnum()`, `isalpha()`, `islower()`, `isupper()`, `istitle()`, `isdecimal()`, `isnumeric()`, `isspace()`.

# 01_Variaveis_e_Tipos_de_Dados 📦 Fundamentos Essenciais

Esta pasta é o ponto de partida para o seu aprendizado em Python, focando nos blocos de construção mais básicos: **Variáveis e Tipos de Dados**. Aqui, você entenderá como armazenar informações, quais os diferentes tipos de dados que o Python reconhece (números, textos, booleanos, etc.) e como manipulá-los.

Cada arquivo representa a **resolução de um problema** que te ajudará a fixar esses conceitos fundamentais.

---

### Conteúdo dos Arquivos:

* [`1_saudacao_personalizada.py`](1_saudacao_personalizada.py) 👋
    * **Problema:** Crie um programa que peça o nome do usuário e exiba uma saudação personalizada (ex: "Olá, Rafael!").
    * **Propósito:** Introduzir a coleta de dados do usuário e a exibição de mensagens formatadas com variáveis.
    * **Conceitos Chave:** `input()` para entrada de texto, `print()` para saída, e variáveis do tipo `string`.

* [`2_analisador_de_tipos.py`](2_analisador_de_tipos.py) 🧐
    * **Problema:** Desenvolva um programa que receba qualquer coisa digitada pelo usuário e mostre na tela qual é o tipo primitivo desse dado.
    * **Propósito:** Entender como Python lida automaticamente com tipos de dados e como verificar o tipo de uma variável.
    * **Conceitos Chave:** `input()`, função `type()`, e a natureza dinâmica dos tipos em Python.

* [`3_analisador_de_string.py`](3_analisador_de_string.py) 🔡
    * **Problema:** Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
    * **Propósito:** Explorar as características básicas de uma `string` e como testar suas propriedades iniciais.
    * **Conceitos Chave:** `input()`, `type()`, e métodos iniciais de `string` (ex: `.isnumeric()`, `.isalpha()`, `.isalnum()`, `.isspace()`).

* [`4_analisador_de_string_completo.py`](4_analisador_de_string_completo.py) 🕵️
    * **Problema:** Aprimore o analisador de string para verificar se o que foi digitado é alfabético, numérico, alfanumérico, está em maiúsculas, minúsculas, capitalizado, ou é composto apenas por espaços.
    * **Propósito:** Aprofundar o conhecimento em diversos métodos de teste de string.
    * **Conceitos Chave:** `str` métodos (`.isalpha()`, `.isnumeric()`, `.isalnum()`, `.islower()`, `.isupper()`, `.isspace()`, `.istitle()`).

* [`5_analisador_de_nome.py`](5_analisador_de_nome.py) 👤
    * **Problema:** Peça o nome completo de uma pessoa e analise-o, mostrando: o nome em maiúsculas e minúsculas, quantas letras tem no total (sem espaços) e quantas letras tem o primeiro nome.
    * **Propósito:** Praticar a manipulação de strings para extrair e formatar informações de um nome completo.
    * **Conceitos Chave:** `input()`, `str` métodos (`.upper()`, `.lower()`, `.strip()`, `.split()`), e a função `len()`.

* [`6_analisador_de_frase.py`](6_analisador_de_frase.py) 💬
    * **Problema:** Crie um programa que leia uma frase e diga: quantas vezes a letra "A" aparece, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
    * **Propósito:** Focar em métodos de string para buscar e contar caracteres específicos dentro de uma frase.
    * **Conceitos Chave:** `str` métodos (`.count()`, `.find()`, `.rfind()`), e normalização de texto (`.upper()` ou `.lower()`).

* [`7_verificador_cidade_santo.py`](7_verificador_cidade_santo.py) ⛪
    * **Problema:** Peça o nome de uma cidade e verifique se o primeiro nome dela é "Santo".
    * **Propósito:** Utilizar métodos de string para verificar o início de um texto e realizar comparações.
    * **Conceitos Chave:** `input()`, `str` métodos (`.strip()`, `.split()`, `.startswith()`), e operadores de comparação.

* [`8_extrator_nome_sobrenome.py`](8_extrator_nome_sobrenome.py) 🏷️
    * **Problema:** Peça o nome completo de uma pessoa e mostre separadamente o primeiro nome e o último sobrenome.
    * **Propósito:** Praticar a divisão de strings e o acesso a elementos específicos de uma lista resultante.
    * **Conceitos Chave:** `input()`, `str` método `.split()`, e acesso a elementos de lista por índice (`[0]`, `[-1]`).
