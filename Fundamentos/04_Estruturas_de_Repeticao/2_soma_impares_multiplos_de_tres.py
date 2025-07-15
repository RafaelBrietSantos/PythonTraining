# ----- EXPLICANDO -----
# Para entender como esse código funciona, vamos pensar no 'soma' como uma sacola.

soma = 0 # Esta é a "sacola da soma": ela começa vazia (com o valor 0).
         # Nela, vamos guardar a soma de todos os números que encontrarmos.
cont = 0 # Esta é a "sacola do contador": ela também começa vazia (com o valor 0).
         # Nela, vamos contar quantos números foram encontrados.

# O loop 'for' vai iterar de 1 até 500 (inclusive), pulando de 2 em 2.
# Isso significa que ele vai passar apenas por números ÍMPARES (1, 3, 5, ..., 499).
for c in range(1, 501, 2):
    # A cada número 'c' que o loop encontra, ele verifica uma condição:
    # 'if c % 3 == 0:' - Isso checa se o número 'c' é um MÚLTIPLO DE 3.
    # O operador '%' (módulo) retorna o resto da divisão. Se o resto for 0, é divisível.
    if c % 3 == 0:
        # Se 'c' for ímpar E múltiplo de 3 (ex: 3, 9, 15, ...):
        
        # 'cont += 1' - Adiciona 1 à nossa "sacola do contador".
        # É o mesmo que 'cont = cont + 1'. Estamos contando quantos números atendem à condição.
        cont += 1
        
        # 'soma += c' - Adiciona o valor do número 'c' à nossa "sacola da soma".
        # É o mesmo que 'soma = soma + c'. Estamos pegando o número 'c' e colocando na sacola da soma.
        soma += c

# Após o loop terminar de verificar todos os números de 1 a 500,
# exibe o total de números encontrados e a soma total deles.
print('A soma de todos os {} números solicitados é {}.'.format(cont, soma))