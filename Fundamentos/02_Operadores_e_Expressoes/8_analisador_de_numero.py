# Pede ao usuário para digitar um número inteiro.
# 'int()' é fundamental aqui para garantir que possamos fazer operações matemáticas.
num = int(input("Digite um número: "))

print("Analisando o número...")

# Unidade:
# Usamos o operador de MÓDULO (%). Ele retorna o RESTO da divisão.
# num % 10 -> Pega o resto da divisão de 'num' por 10. Para qualquer número inteiro,
# o resto da divisão por 10 será sempre o último dígito (a unidade).
# Ex: 123 % 10 = 3
print("Unidade: {}".format(num % 10))

# Dezena:
# Primeiro, 'num // 10'. O operador de DIVISÃO INTEIRA (//) retorna a parte inteira da divisão.
# Isso "remove" o último dígito do número.
# Ex: 123 // 10 = 12
# Depois, aplicamos o MÓDULO por 10 novamente sobre o resultado (12 % 10 = 2).
# Isso isola o dígito da dezena.
print("Dezena: {}".format(num // 10 % 10))

# Centena:
# Segue a mesma lógica. 'num // 100' "remove" os dois últimos dígitos.
# Ex: 1234 // 100 = 12
# Em seguida, '12 % 10' isola o dígito da unidade desse novo número (que é a centena original).
# Ex: 12 % 10 = 2
print("Centena: {}".format(num // 100 % 10))

# Milhar:
# 'num // 1000' "remove" os três últimos dígitos.
# Ex: 12345 // 1000 = 12
# E '12 % 10' isola o dígito da milhar.
# Ex: 12 % 10 = 2
print("Milhar: {}".format(num // 1000 % 10))