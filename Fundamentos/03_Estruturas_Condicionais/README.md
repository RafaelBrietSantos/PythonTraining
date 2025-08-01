<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="100"/>
</p>

# 🚦 Decisões Inteligentes: Dominando as Estruturas Condicionais em Python! 🧠
## 03_Estruturas_Condicionais 💡

**Seja bem-vindo(a) ao mundo onde seu código toma decisões!** ✨

Nesta pasta, exploraremos as **Estruturas Condicionais** em Python, a espinha dorsal de qualquer programa que precisa agir de forma diferente em situações distintas. Você aprenderá a guiar o fluxo do seu código, fazendo-o "pensar" e executar comandos específicos **se** certas condições forem verdadeiras, **ou então** seguir outros caminhos.

Aqui, o `if`, `elif` e `else` se tornarão seus melhores amigos, permitindo que você crie programas mais dinâmicos e inteligentes, capazes de reagir a diferentes entradas e cenários. Cada arquivo é um **desafio resolvido** que te dará o poder da escolha na programação!

---

### Conteúdo dos Arquivos:

* [`1_verificador_nome_briet.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/1_verificador_nome_briet.py) 🕵️
    * **Problema:** Crie um programa que peça um nome e verifique se ele contém a palavra "Briet" (ignorando maiúsculas/minúsculas).
    * **Propósito:** Verifica se um nome digitado pelo usuário contém a palavra "Briet".
    * **Conceitos Chave:** `input()`, `strip()`, `title()`, `lower()`, operador `in` para busca de substrings, e a estrutura **`if`/`else`** para tomada de decisão.

* [`2_radar_eletronico.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/2_radar_eletronico.py) 🚓
    * **Problema:** Simule um radar de velocidade. Peça a velocidade de um carro e, se ela exceder 80 Km/h, calcule e informe o valor da multa (R$7,00 por cada Km acima do limite).
    * **Propósito:** Simula um radar de velocidade, multando o motorista se a velocidade exceder o limite.
    * **Conceitos Chave:** `input()`, `float()`, **`if`/`else`** para aplicar regras (multa ou não), e cálculos simples.

* [`3_verificador_ano_bissexto.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/3_verificador_ano_bissexto.py) 🗓️
    * **Problema:** Desenvolva um programa que leia um ano qualquer (ou use o ano atual da máquina) e mostre se ele é um ano bissexto.
    * **Propósito:** Verifica se um ano fornecido pelo usuário é bissexto, seguindo as regras específicas de anos bissextos.
    * **Conceitos Chave:** `input()`, `int()`, importação do módulo `datetime` (`date.today().year`), e **condições complexas** com operadores lógicos (`and`, `or`).

* [`4_calculadora_passagem.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/4_calculadora_passagem.py) 🚌💸
    * **Problema:** Crie um programa para calcular o preço de uma passagem. Se a viagem for até 200 Km, o preço é R$0.50/Km. Para viagens mais longas, o preço é R$0.45/Km.
    * **Propósito:** Calcula o preço de uma passagem de ônibus, aplicando tarifas diferentes com base na distância da viagem.
    * **Conceitos Chave:** `input()`, `int()`, e **`if`/`else`** para aplicar regras de precificação por quilometragem.

* [`5_verificador_de_triangulo.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/5_verificador_de_triangulo.py) 三角形
    * **Problema:** Receba o comprimento de três retas e informe ao usuário se elas podem ou não formar um triângulo.
    * **Propósito:** Determina se três segmentos de reta informados pelo usuário podem formar um triângulo.
    * **Conceitos Chave:** `input()`, `float()`, **condições aninhadas** com operadores lógicos (`and`) para a regra de existência de triângulos, e **formatação de texto no terminal** (cores ANSI).

* [`6_verificador_par_ou_impar.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/6_verificador_par_ou_impar.py) 🔢❓
    * **Problema:** Escreva um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.
    * **Propósito:** Verifica se um número inteiro digitado pelo usuário é par ou ímpar.
    * **Conceitos Chave:** `input()`, `int()`, e o **operador de módulo (`%`)** combinado com **`if`/`else`** para identificar a paridade.

* [`7_calculadora_aumento_salario.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/7_calculadora_aumento_salario.py) 💰📈
    * **Problema:** Calcule o aumento de salário para funcionários. Salários superiores a R$1.250,00 recebem 10% de aumento. Para salários inferiores ou iguais, o aumento é de 15%.
    * **Propósito:** Calcula o novo salário de um funcionário com base em diferentes percentuais de aumento, dependendo do salário atual.
    * **Conceitos Chave:** `input()`, `int()` (ou `float()`), e **`if`/`else`** para aplicar regras de reajuste salarial.

* [`8_comparador_de_numeros.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/8_comparador_de_numeros.py) 🔢⚖️
    * **Problema:** Leia dois números inteiros e compare-os, mostrando qual é o maior, qual é o menor ou se são iguais.
    * **Propósito:** Praticar o uso de múltiplas condições (`if`/`elif`/`else`) para comparar valores.
    * **Conceitos Chave:** `input()`, `int()`, operadores de comparação (`>`, `<`, `==`), e estrutura `if`/`elif`/`else`.

* [`9_alistamento_militar.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/9_alistamento_militar.py) 🎖️
    * **Problema:** Faça um programa que leia o ano de nascimento de um jovem e informe seu status de alistamento militar: se ainda vai se alistar, se é a hora, ou se já passou do tempo.
    * **Propósito:** Calcular a idade e usar condições para determinar o status de alistamento militar, incluindo a diferença de tempo.
    * **Conceitos Chave:** `input()`, `int()`, `datetime` para ano atual, cálculos de idade, e `if`/`elif`/`else` com diferentes cenários.

* [`10_classificador_atletas.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/10_classificador_atletas.py) 🏊‍♂️🏆
    * **Problema:** Crie um programa que leia o ano de nascimento de um atleta e classifique-o em categorias (mirim, infantil, júnior, sênior, master) de acordo com a idade.
    * **Propósito:** Classificar atletas em categorias de idade usando múltiplas condições.
    * **Conceitos Chave:** `input()`, `int()`, `datetime` para ano atual, cálculo de idade, e `if`/`elif`/`else` para faixas etárias.

* [`11_calculadora_imc.py`](https://github.com/RafaelBrietSantos/PythonTraining/blob/main/Fundamentos/03_Estruturas_Condicionais/11_calculadora_imc.py) ⚖️🍎
    * **Problema:** Calcule o Índice de Massa Corporal (IMC) de uma pessoa, pedindo o peso e a altura, e mostre seu status de acordo com a tabela padrão de IMC.
    * **Propósito:** Calcular o IMC e classificar o resultado em categorias de saúde usando condições.
    * **Conceitos Chave:** `input()`, `float()`, cálculo de IMC (`peso / (altura ** 2)`), e `if`/`elif`/`else` para classificar o IMC.
