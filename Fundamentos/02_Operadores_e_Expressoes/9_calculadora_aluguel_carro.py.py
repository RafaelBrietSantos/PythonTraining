#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input('quantos dias foram alugados? '))
km = float(input('Quantos km foi rodado? ' ))

# dia= R$60 e km = R$0,15
#if dias >= 2  km >= 2:
#   dias * 60

#else:
#    print("")
# poderia deixar igual esta qui em baixo porem oq eu deixei é mais facil
#co3 = dias * 60
#co2 = km * 0.15
#ter = (co2 + co3) #Custo total final 
co= (dias * 60) + (km * 0.15)
#sei que não precisa dos () porem coloquei pra deixar organizado
print('O aluguel do carro ficou em: {} '.format(co))

# Não ultiliza vergula em numero e sim um .  (ex: 0.15 e não 0,15) e eu sofri pra descobrir isso 