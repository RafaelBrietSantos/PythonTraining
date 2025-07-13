# Pede a distância da viagem ao usuário e converte para um número inteiro.
dis = int(input('Qual a distância da viagem (em Km)? '))
dis = int(input ('Qual a distancia da viagem? '))

# Verifica se a distância é IGUAL ou MENOR que 200 Km.
if dis <= 200:
    # Se a condição for verdadeira, o preço por Km é R$ 0.50.
    pre = dis * 0.50
    
else:
    # Se a condição for falsa (ou seja, a distância é MAIOR que 200 Km),
    # o preço por Km é R$ 0.45.
    pre = dis * 0.45
    
# Imprime o preço final da passagem, formatado para duas casas decimais, ideal para valores monetários.
print('O preço da passagem é R${:.2f}'.format(pre))