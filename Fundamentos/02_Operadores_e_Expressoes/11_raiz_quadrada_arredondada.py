import math

num = int(input('Digite um numero:' ))

# calcula a RAIZ QUADRADA
raiz = math.sqrt(num)
                         
print('A raiz de {:.2f} é igual a {:.2f}'.format(num, math.ceil(raiz)))

# # math.sqrt calcula raiz quadrada
# # math.ceil arredonda pra +
# # math.floor arredonda pra - (lembre-se que 'math.floor()' arredonda para baixo)

