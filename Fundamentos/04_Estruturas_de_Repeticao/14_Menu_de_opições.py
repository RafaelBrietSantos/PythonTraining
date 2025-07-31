from time import sleep
num1 = int(input('Digite um numero:'))
num2 = int(input('Digite mais um numero:'))

while True:
    
    print('   [ 1 ] Somar')
    print('   [ 2 ] Multiplicar')
    print('   [ 3 ] Maior')
    print('   [ 4 ] Novo numero')
    print('   [ 5 ] Sair do programa')
    opção = int(input('>>>>> Qual é opção você deseja? '))

    if opção > 5:
        print('Opção invalida. Tente novamente')

    if opção == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é de {soma}')

    if opção == 2:
        multiplicação = num1 * num2
        print(f'A multiplicação de {num1} e {num2} é de {multiplicação}')
    
    if opção == 3:
        if num1 > num2:
            print(f'O {num1} é maior que {num2}.')
        elif num1 < num2:
            print(f'O {num2} é maior que {num1}')
        else:
            print('Os numeros digitados são iguais.')
    
    if opção == 4:
        num1 = int(input('digite o numero novo: '))
        num2 = int(input('digite o proximo: '))
        print('Numeros atualizados com sucesso!')
    

    print('=-=' * 10)
    sleep(2)
    if opção == 5:
        print('Programa encerrado.')
        break
   

