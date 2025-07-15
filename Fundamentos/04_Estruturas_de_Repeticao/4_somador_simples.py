s = 0 
# 's = 0'
# Aqui, você cria uma variável chamada 's' e a inicializa com o valor 0.
# Pense em 's' como uma "sacola da soma" que está vazia no início.
# Ela vai guardar a soma de todos os números que o usuário digitar.

# 'for c in range(0, 4):'
# Este é um loop 'for'. Ele vai se repetir um número específico de vezes.
# 'range(0, 4)' gera uma sequência de números que começa em 0 e vai ATÉ 4, mas não inclui o 4.
# Então, a sequência é: 0, 1, 2, 3.
# Isso significa que o código dentro do loop (as linhas indentadas) será executado 4 vezes.
# 'c' é uma variável que assume esses valores (0 na primeira vez, 1 na segunda, etc.).
for c in range(0, 4):
    # 'n = int(input('digite um numero: '))'
    # A cada repetição do loop, o programa pede ao usuário para digitar um número.
    # 'input()' lê o que o usuário digita (sempre como texto).
    # 'int()' converte esse texto para um número inteiro, e ele é guardado na variável 'n'.
    n = int(input('Digite um numero: '))
    
    # 's += n'
    # Esta é a parte mais importante para a soma.
    # É o mesmo que 's = s + n'.
    # A cada número 'n' que o usuário digita, ele é adicionado (somado) ao valor atual de 's'.
    # É como se você estivesse colocando o número 'n' dentro da sua "sacola da soma" ('s').
    s += n

# 'print ('A somatoria de todos os valores são {}'.format(s))'
# Depois que o loop terminou (ou seja, o usuário digitou os 4 números e eles foram somados),
# esta linha é executada.
# Ela exibe o valor final de 's', que é a soma de todos os números digitados.
print('A somatória de todos os valores é {}'.format(s))