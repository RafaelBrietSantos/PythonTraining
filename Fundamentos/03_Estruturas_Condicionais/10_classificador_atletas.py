import time
nasc = int(input('Digite o ano de nascimento: '))
ano = time.localtime().tm_year #PEegar o ano atual time.localtime().tm_year
idade = ano - nasc
print('O atleta tem {} por isso está ná'.format (idade))

if idade  <= 9:
    print('Classificação: MIRIM ')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
# Se NENHUMA das condições acima for verdadeira (ou seja, idade > 25).
else:
    print('Classificação: MASTER')

    