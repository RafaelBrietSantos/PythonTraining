print('=_=' * 20 )

# Pergunta ao usuário se ele quer calcular o IMC.
# .title() capitaliza a primeira letra para facilitar a comparação (Sim/Não).
res = str(input('vamos calcular seu IMC ? (Sim/Não)')).title()
# Se a resposta for não ja encerra o programa aqui 
if res == 'Não':
    print('Ok, até a proxima')
else:
    print('Vamos la então ')
    # Pede a altura (em metros) e o peso (em quilogramas).
    # float() é usado para permitir números decimais.
    alt = float(input('Digite sua altura: (m) '))
    peso = float(input('Digite seu peso: (kg) '))

     # Calcula o IMC (peso / altura ao quadrado).
    imc = float ( peso / (alt ** 2) )

    # Mostra o IMC calculado 
    print('seu IMC deu {} então'.format (imc))

# --- Estrutura Condicional para Classificação do IMC ---
    # As condições são verificadas em ordem. Uma vez que uma é verdadeira, as outras não são checadas.

if imc <= 18.5:  
    print('Você está abaixo do pesso CUIDADO!')
elif imc <= 18.6 < 24,9:
    print('Você  está no peso NORMAL')
elif imc <= 25 < 29.9:
    print('você está SOBREPESO ')
elif imc <= 30 < 34.9:
    print('Você está OBESIDADE GRAU I')
elif imc <= 35 < 39.9:
    print('Você está OBESIDADE GRAU II')
else:
    print('Você está OBESIDADE GRAU III')
        