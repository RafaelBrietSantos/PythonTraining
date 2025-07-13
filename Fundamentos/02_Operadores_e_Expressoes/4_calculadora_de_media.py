nota1 = float(input('digite sua primeira nota '))
nota2 = float(input('digite a segunda'))
# Calculamos a média.
# A soma (nota1 + nota2) é feita primeiro por causa dos parênteses,
# e depois o resultado é dividido por 2.
resultado  = (nota1 + nota2) / 2

print('sua media entre {} e {} é igual a {}'.format(nota1, nota2, (nota1 + nota2) / 2))
'''            ou pode fazer assim:
print(f'Sua média entre {nota1} e {nota2} é igual a {resultado}')'''