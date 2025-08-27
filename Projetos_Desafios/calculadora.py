
while True:
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-/*): ')
    
    print('\n')

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None

    
    if num_validos is None:
        print('Um ou ambos digitos digitados não são validos')
        print('\n')
        continue


    operador_permitido = ['+','-','/','*']
    if operador not in operador_permitido:
        print('Operados invalido')
        print('\n')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        print('\n')
        continue

    if operador == '+':
        conta = num1_float + num2_float
        print(f'{num1} {operador} {num2} = {conta}')

    elif operador == '-':
        conta = num1_float - num2_float
        print(f'{num1} {operador} {num2} = {conta}')

    elif operador == '/':
        conta = num1_float / num2_float
        print(f'{num1} {operador} {num2} = {conta}')

    elif operador == '*':
        conta = num1_float * num2_float 
        print(f'{num1} {operador} {num2} = {conta}')


 

    #Sair
    

    # Se digitar algo que comesse com 's' ele vai dar True 
    print('\n')
    sair = input('Deseja sair? [S]im: ').lower().startswith('s')

    if sair is True:
        break
