vel = float(input('Qual é a velocidade do carro? '))
if vel > 80:
    # Se a velocidade for maior que 80, o carro está multado.
    print('MULTADO! Você excedeu o limire permitido que é de 80km/h')
     #
     # Pode deixar o print assim tbm --> print('Você deve pagar uma multa de R${:.2f}!'.format(vel * 7))
    multa = 7 * vel
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

else:
    # Se a velocidade não for maior que 80 (ou seja, for 80 ou menos)
    print('Velocidade permitida ')
print('Tenha um bom dia! Dirija com segurança!')