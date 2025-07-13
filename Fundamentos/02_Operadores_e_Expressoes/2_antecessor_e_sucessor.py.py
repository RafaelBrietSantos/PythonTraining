# Pedimos ao usuário para digitar um número inteiro.
# É crucial converter a entrada para 'int' (inteiro) com int(),
# pois 'input()' sempre retorna uma string. Se não convertêssemos,
# Python tentaria subtrair ou somar strings, o que causaria um erro.
n = int(input('Digite um número: '))

# --- Opção 1: Usando variáveis auxiliares para antecessor e sucessor ---
# Esta forma é mais explícita e pode ser mais fácil de ler para iniciantes,
# pois cada cálculo é armazenado em sua própria "caixinha" (variável).
# ant = n - 1 # Calcula o antecessor subtraindo 1 de 'n'
# dep = 1 + n # Calcula o sucessor somando 1 a 'n'

# print ('Analisando o valor {} seu antecessor é {} e seu sucessor é {}'.format(n, ant, dep))

# --- Opção 2: Calculando diretamente dentro do print (a sua escolha!) ---
# Esta forma é mais concisa, pois os cálculos de (n-1) e (1+n) são feitos
# "na hora" dentro do próprio comando 'print'. O resultado é o mesmo.
# É uma questão de estilo e legibilidade para quem está lendo o código.
print ('Analisando o valor {} seu antecessor é {} e seu sucessor é {}'.format(n, n-1, 1+n))

# A f-string é outra excelente forma de fazer isso, mais moderna e legível:
# print(f'Analisando o valor {n} seu antecessor é {n-1} e seu sucessor é {n+1}')