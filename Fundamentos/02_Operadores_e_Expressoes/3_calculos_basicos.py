n = int(input ('digite um numero: '))
print ('o dobro de {} é de {}'.format(n, n*2))
print ('o triplo de {} é de {}'.format(n, n*3))
#pra fazer araiz quadrada eu tenho que por <  variavel **(1/2)    > como o exemplo abaixo 
print ('a raiz de {} é {}'.format(n, n **(1/2)))

'''obs:'''
# Outra forma de calcular a raiz quadrada é usando o módulo 'math'.
# Primeiro, importamos o módulo math.
#import math
# print('A raiz quadrada (usando math.sqrt) de {} é {:.2f}'.format(n, math.sqrt(n)))
# O ':.2f' formata o resultado para ter duas casas decimais, o que é útil para raízes.
