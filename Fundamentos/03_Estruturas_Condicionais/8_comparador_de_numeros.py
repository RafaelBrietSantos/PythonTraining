n1 = int(input('Primero numero:'))
n2 = int(input('segundo numero:'))

# Primeira vez usando o elif

# --- Estrutura Condicional: if / elif / else ---

# Primeira condição: Verifica se o 'n1' é MAIOR que 'n2'.
# Se esta condição for verdadeira, executa o bloco e encerra a verificação.
if n1 > n2:
    print('O PRIMEIRO número é maior.')
# Segunda condição ('elif' = "else if"): Se a primeira condição for falsa,
# verifica se 'n1' é IGUAL a 'n2'.
# Se esta condição for verdadeira, executa o bloco e encerra a verificação.
elif n1 == n2:
    print('Os dois números são iguais.')
# Última condição ('else'): Se NENHUMA das condições anteriores for verdadeira (n1 não é maior, nem igual a n2),
# então 'n1' só pode ser MENOR que 'n2'.
# Executa este bloco como a opção final.
else:
    print('O SEGUNDO número é maior.')