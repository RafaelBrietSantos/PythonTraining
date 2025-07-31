def saudacao(nome):
    print(f'Ola {nome}!')

print('\n Chamando a função saudacao')
saudacao('Alice')
saudacao('Bob')

def quadrado(numero):
    resultado = numero ** 2 
    return resultado
print('\n Chamando função resultado: ')
resultado = quadrado(5)
print(f'Resultado da função quadrada: {resultado}',)

def soma(num1, num2):
    conta = num1 + num2
    return conta
resultado = soma(20, 40)
print('\n',resultado)