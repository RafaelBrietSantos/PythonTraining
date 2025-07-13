# So para decorar
print('-=' * 20)

# Pede os três segmentos de reta.
# Usamos 'float()' para permitir medidas com casas decimais.
r1 = float(input('digite um seguimento pro triangulo '))
print('-=' * 20)
r2 = float(input('digite outro seguimento pro triangulo '))
print('-=' * 20)
r3 = float(input('digite mais um seguimento pro triangulo '))
print('-=' * 20)

#     Lógica para verificar a formação de um triângulo 
# A regra para formar um triângulo é:
# A soma do comprimento de quaisquer dois lados deve ser maior que o comprimento do terceiro lado.
# Você aplicou essa regra corretamente com três condições 'AND':
# 1. r1 < r2 + r3 (O primeiro lado é menor que a soma dos outros dois)
# 2. r2 < r1 + r3 (O segundo lado é menor que a soma dos outros dois)
# 3. r3 < r1 + r2 (O terceiro lado é menor que a soma dos outros dois)
# Se TODAS as três condições forem VERDADEIRAS, o triângulo pode ser formado.


cal = r3 + r2 
if r1 < cal and r2 < r1 + r3 and r3 < r1 + r2:
    # Se a condição for verdadeira, imprime uma mensagem colorida.
    print('\033[0;35mOs seguimentos acima podem formar um triangulo\033[m')
else:
    # Se a condição for falsa, imprime uma mensagem indicando que não pode formar um triângulo.
    print('Não pode se transformar entriangulo ')
