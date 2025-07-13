num = int(input('Digite um numero: '))

#          A lógica de par ou ímpar 
# Para verificar se um número é par, precisamos saber se ele tem resto 0 quando dividido por 2.
# O operador de MÓDULO (%) é perfeito para isso, pois ele retorna o RESTO da divisão.
# Ex:
# 10 % 2 = 0 (10 é par)
# 7 % 2 = 1 (7 é ímpar)

cal = num % 2 # Se o resto da divisão por 2 for 0, o número é par.
if cal == 0:
    print ('esse numero {} é PAR '.format (num))
else: # Caso contrário (o resto é 1), o número é ímpar.
    print('Esse nummero {} é IMPAR'.format (num))