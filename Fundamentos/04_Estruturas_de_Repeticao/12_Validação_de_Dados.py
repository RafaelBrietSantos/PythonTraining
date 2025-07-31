sexo = input('Informe seu sexo: [M/F] ') .upper().strip()[0]

while True:
    
    if sexo == 'M' or sexo == 'F':
        print(f'Sexo {sexo} registrado com sucesso')
        break
    else:
        sexo = input('Dados inválidos. Por favor, informe seu sexo: ') .upper().strip()[0]

        