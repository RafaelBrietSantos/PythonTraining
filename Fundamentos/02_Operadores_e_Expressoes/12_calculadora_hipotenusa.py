import math
import emoji

cat1 = float(input('Digite o valor do cateto: '))
cat2 = float(input('Digite o valor do cateto adijacente: '))
# Tem varias formas de c fazer isso
# hip = (cat1 ** 2 + cat2 ** 2) ** (1/2)

#  2 Usando funções do módulo math (pow e sqrt):
#res = math.pow (cat1, 2)
#res2 = math.pow (cat2, 2)
#cal = res + res2
#hip = math.sqrt(cal)

#  3 Usando a função math.hypot() 
hip = math.hypot(cat1, cat2)

print(emoji.emojize('O valor da hipotenusa é de {:.2} :smiley:'.format(hip), language='alias'))
