# Importa o módulo 'math' completo.
# Este módulo contém muitas funções matemáticas avançadas, incluindo trigonométricas.

import math


ang = int(input('Digite um angulo: '))
# Converter o graus pra radianos
rad = math.radians(ang)

# Calcula o seno do ângulo (em radianos)
sen = math.sin(rad)

# Calcula o cosseno do ângulo (em radianos)
con = math.cos(rad)

# Calcula a tangente do ângulo (em radianos).
tan = math.tan(rad)

# Exibe os resultados formatados.
# O '{:.2f}' formata os números para ter 2 casas decimais, o que é ótimo para resultados trigonométricos.
print('    Com o angulo {} conseguimos decobrir que:'.format(ang))
print('  o seno dele é {:.2f} o coseno é {:.2f} e o tangente é {:.2f}'.format(sen, con, tan))