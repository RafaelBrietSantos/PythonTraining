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

* **`04_analisador_de_nome.py`** 👤
    * **Propósito:** Pede o nome completo de uma pessoa e apresenta o nome em diferentes formatos (maiúsculas, minúsculas) e a contagem de letras do primeiro nome e do nome completo (sem espaços).
    * **Conceitos Chave:** `input()`, `strip()`, `title()`, `upper()`, `lower()`, `split()`, `len()`, e `join()`. Aborda a manipulação e transformação de strings em **listas**.

* **`05_extrator_nome_sobrenome.py`** ✂️
    * **Propósito:** Solicita um nome completo e extrai e exibe apenas o primeiro e o último nome.
    * **Conceitos Chave:** `input()`, `strip()`, `title()`, `split()`, e o **acesso a elementos de listas por índice** (incluindo o uso de índices negativos como `[-1]` para o último elemento).

* **`06_analisador_de_frase.py`** 📝
    * **Propósito:** Permite ao usuário digitar uma frase e uma letra, e então informa quantas vezes a letra aparece e em quais posições (primeira e última).
    * **Conceitos Chave:** `input()`, `strip()`, `lower()`, `count()`, `find()`, e `rfind()` para busca e análise de substrings.

* **`07_verificador_cidade_santo.py`** 📍
    * **Propósito:** Verifica se o nome de uma cidade, digitado pelo usuário, começa com o prefixo "Santo".
    * **Conceitos Chave:** `input()`, `strip()`, `title()`, `lower()`, e o método de string `startswith()` para verificação de prefixos.

---

**Sugestão de Melhoria Visual (para o futuro):**

Você pode adicionar uma imagem no topo do seu `README.md` para deixá-lo ainda mais atraente. Por exemplo, uma imagem que represente "Fundamentos de Python". Para isso, você precisaria:

1.  Ter a imagem (ex: `python_basics.png`) na mesma pasta do `README.md` ou em uma subpasta (`assets/python_basics.png`).
2.  Adicionar uma linha como esta no topo do `README.md`:

    ```markdown
    ![Título da Imagem](caminho/para/sua/imagem.png)
    ```

    Exemplo: `![Fundamentos de Python](python_basics.png)` ou `![Fundamentos de Python](assets/python_basics.png)`

---

