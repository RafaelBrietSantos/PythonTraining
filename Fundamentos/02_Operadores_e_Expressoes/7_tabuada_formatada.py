# Pede ao usuário um número inteiro para a tabuada, como no código anterior.
n = int(input('Digite um número para a tabuada: '))

# Imprime uma linha separadora.
print('-----------------------')

# Imprime cada linha da tabuada de 1 a 10.
# A GRANDE DIFERENÇA AQUI é o '{:2}'.
# Isso significa que o número (1, 2, 3... 10) será formatado para ocupar 2 espaços.
# Se o número tiver apenas 1 dígito (como '1'), ele será precedido por um espaço.
# Isso ajuda a manter as colunas mais alinhadas, especialmente quando o '10' aparece.
print('  {} X  {:2} = {}'.format(n, 1, n*1))
print('  {} X  {:2} = {}'.format(n, 2, n*2))
print('  {} X  {:2} = {}'.format(n, 3, n*3))
print('  {} X  {:2} = {}'.format(n, 4, n*4))
print('  {} X  {:2} = {}'.format(n, 5, n*5))
print('  {} X  {:2} = {}'.format(n, 6, n*6))
print('  {} X  {:2} = {}'.format(n, 7, n*7))
print('  {} X  {:2} = {}'.format(n, 8, n*8))
print('  {} X  {:2} = {}'.format(n, 9, n*9))
print('  {} X  {:2} = {}'.format(n, 10, n*10))

# Imprime outra linha separadora.
print('-----------------------')