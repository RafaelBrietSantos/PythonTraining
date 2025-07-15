# 04_Estruturas_de_Repeticao 🔄 Loops e Iteração

Esta pasta é o seu playground para dominar as **Estruturas de Repetição (Loops)** em Python. Aqui, você aprenderá como automatizar tarefas repetitivas, iterar sobre sequências de dados e criar programas que executam ações múltiplas vezes sem precisar reescrever o código.

Você verá exemplos práticos do uso do loop **`for`**, que é ideal para quando você sabe (ou pode determinar) o número de vezes que uma ação precisa ser repetida. Cada arquivo representa a **resolução de um problema** específico.

---

### Conteúdo dos Arquivos:

* [`1_contagem_pares.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/1_contagem_pares.py) 🔢
    * **Problema:** Crie um programa que mostre na tela todos os números pares que estão entre 0 e 50.
    * **Propósito:** Demonstra o uso básico do `for` e `range()` para gerar uma sequência de números pares em um intervalo.
    * **Conceitos Chave:** `for` loop, função `range()` com passo (`step`), e `print()` com `end=' '` para formatar a saída na mesma linha.

* [`2_soma_impares_multiplos_de_tres.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/2_soma_impares_multiplos_de_tres.py)) ➕
    * **Problema:** Desenvolva um programa que calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
    * **Propósito:** Soma e conta números que atendem a múltiplas condições (ímpar e múltiplo de três) em um intervalo.
    * **Conceitos Chave:** `for` loop, `if` condicional dentro de um loop, **acumuladores** (`soma += c`), **contadores** (`cont += 1`), e o operador de módulo (`%`).

* [`3_somador_simples.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/3_testando_o_for.py)) 📥
    * **Problema:** Faça um programa que peça ao usuário para digitar 4 números inteiros e, ao final, mostre a somatória de todos esses valores.
    * **Propósito:** Pede ao usuário para digitar múltiplos números e calcula a soma total desses valores.
    * **Conceitos Chave:** `for` loop para repetir a entrada de dados, `input()` dentro do loop, e um **acumulador** (`s += n`) para somar os valores digitados.

* [`4_range_dinamico.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/4_somador_simples.py)) ⚙️
    * **Problema:** Crie um programa que permita ao usuário definir o início, o fim e o passo de uma contagem, e então exiba todos os números dessa sequência.
    * **Propósito:** Permite ao usuário definir o início, o fim e o passo de uma contagem, mostrando a flexibilidade do `range()`.
    * **Conceitos Chave:** `for` loop, `range()` com três argumentos (`início`, `fim`, `passo`), e `input()` para controle dinâmico do loop.

* [`5_contagem_regressiva.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/5_range_dinamico.py)) 🚀
    * **Problema:** Simule uma contagem regressiva de 10 a 1, com um segundo de pausa entre cada número, finalizando com uma mensagem de "Feliz Ano Novo!".
    * **Propósito:** Cria uma contagem regressiva, simulando uma virada de ano, com pausas entre os números.
    * **Conceitos Chave:** `for` loop com `range()` em passo negativo para contagem decrescente, e o módulo `time.sleep()` para introduzir atrasos na execução.

* [`6_contador_numeros_primos.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/6_contagem_regressiva.py)) ⭐
    * **Problema:** Desenvolva um programa que identifique e conte quantos números primos existem no intervalo de 1 a 100.
    * **Propósito:** Encontra e conta os números primos em um intervalo definido.
    * **Conceitos Chave:** **Loops aninhados** (`for` dentro de `for`), `if` condicional para verificar divisores, e o conceito de **números primos** (exatamente dois divisores).

* [`7_primos_ate_numero_dado.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/7_contador_numeros_primos.py)) 🔍
    * **Problema:** Crie um programa que peça um número ao usuário e então liste todos os números de 1 até esse valor, indicando quais são primos e quais não são.
    * **Propósito:** Verifica e lista quais números até um valor digitado pelo usuário são primos ou não.
    * **Conceitos Chave:** Loops aninhados para testar cada número, reinicialização de contadores dentro de loops, e formatação de texto no terminal.

* [`8_gerador_pa.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/8_primos_ate_numero_dado.py)) 📈
    * **Problema:** Elabore um programa que solicite o primeiro termo e a razão de uma Progressão Aritmética (PA) e exiba os 10 primeiros termos dessa sequência.
    * **Propósito:** Gera os 10 primeiros termos de uma Progressão Aritmética (PA) a partir de um termo inicial e uma razão.
    * **Conceitos Chave:** `for` loop, `range()` com três argumentos, cálculo do n-ésimo termo de uma PA, e `print()` com `end=' '` para formatar a saída da sequência.

* [`9_soma_pares_ou_impares.py`]((https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/04_Estruturas_de_Repeticao/9_gerador_pa.PY)) ⚖️
    * **Problema:** Faça um programa que peça 6 valores inteiros ao usuário. Ao final, ele deve somar e contar apenas os números ímpares que foram digitados.
    * **Propósito:** Pede ao usuário para digitar uma série de números e soma/conta apenas aqueles que são ímpares (ou pares, dependendo da lógica do `if`).
    * **Conceitos Chave:** `for` loop para iterações fixas, `input()` dentro do loop, `if` condicional para filtrar valores, e **acumuladores/contadores**.
