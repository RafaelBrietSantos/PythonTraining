"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
while True:
    entrada = input('digite um numero: ')
    if entrada.isdigit():
        entrada_int = int(entrada)
        par = entrada_int  % 2 == 0
        par_impar_texto = 'impar'
       
        if par :
            par_impar_texto = 'par'
        
        print(f'O numero {entrada_int} é {par_impar_texto}')
        break

    else:
        print('Dado não inteiro... Digite novamente')





"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""



while True:
    try:
        entrada = input('Digite as horas em números inteiros (0-23): ')
        hora = int(entrada)
        if hora >= 0 and hora <= 11:
            print('\n\nBom dia')
            break
        elif hora >= 12 and hora <= 17:
            print('\n\nBoa tarde')
            break
        elif hora >= 18 and hora <= 23:
            print('\n\nBoa noite')
            break
        elif hora == str:
            print('\n\nNão conheço essa hora')
        else:
            print('\n\nNão conheço essa hora ')
            entrada = input('Digite as horas em numeros INTEIROS? ')
    except ValueError:
        print('\nEntrada inválida. Por favor, digite apenas números inteiros.')
        


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input('Digite seu primeiro nome: ')


numero = len(nome)



if numero <= 4:
    print("Seu nome é curto")

elif numero >= 5 and numero <= 6:
    print("Seu nome é normal")

elif numero > 6:
    print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

