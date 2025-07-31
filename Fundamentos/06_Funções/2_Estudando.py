def divisão (num1, num2):
    return num1 / num2
resultado = divisão(4,2)
print(resultado)

#---------------------------------

def media (notas1, notas2, notas3, notas4, notas5):
    return (notas1 + notas2 + notas3 + notas4 + notas5) / 5

nota1 = int(input('digita sua nota: '))
nota2 = int(input('digita sua nota: '))
nota3 = int(input('digita sua nota: '))
nota4 = int(input('digita sua nota: '))
nota5 = int(input('digita sua nota: '))

medi = media(nota1, nota2, nota3, nota4, nota5) # <-- essa linha serve pra :
                                                #                           Executar a função que faz o cálculo.
                                                #                           Armazenar o resultado desse cálculo em uma variável.
                                                #                           Imprimir o resultado dessa variável depois.

print(medi)
print('\n')

#--------------------------------

# Função cm argumentos arbitrarios, *args
def FrutaPreferida(*fruta):       # Fala  que 'fruta virou uma caixa'
# [0] aqui é pra falar qual é a fruta 0 == banana 1 == Goiba e assim por diante... 
    print('Eu gosto de ',fruta[0])                                  
    print('Eu gosto de ',fruta[1])
    print('Eu gosto de ',fruta[2])
    print('Eu gosto de ',fruta[3])

                    # Coloquei frutas na caixa
FrutaPreferida('Banana', 'Goiaba', 'Laranja', 'Kiwi')


def UnirLista(*lista):
    print(lista)
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

UnirLista(*lista1, *lista2)

# Se a palavra chav for decosnhecido
# Adicionamos ** antes do nome do parametro

def funcaoKwargs(**parametro):
    print('Eu moro em', parametro['cidade1'])
    print('Eu moro em', parametro['cidade2'])

funcaoKwargs(cidade1 = 'SP', cidade2 = 'RJ')

