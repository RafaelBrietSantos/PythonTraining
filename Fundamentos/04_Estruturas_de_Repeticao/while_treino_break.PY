while True: #True sempre vai ser verdadeiro então ele seria infinito se não tivesse o break
    numero = int(input('digite um numero par: '))
    if numero % 2 == 0:
        print('Obrigado por digita um numero par')
        break # Serve para parar o loop, mesmo estando na condição 'True'
              # Essencial para parar loops infinitos ou quando uma condição específica é atingida.
    else:
        print('ERROU tente novamente: ')

print('Fim do Programa')
