# Importa o módulo 'random'.
# Ele contém funções para gerar números aleatórios ou fazer escolhas aleatórias, como vamos ver.
import random

# Importa o módulo 'emoji'.
# Este módulo permite usar códigos de texto para exibir emojis.
# Lembre-se: se você não instalou o módulo 'emoji' ainda, precisará fazer isso no seu terminal:
# pip install emoji
import emoji

# Pede o nome de 5 alunos e guarda cada um em uma variável.
nome = input('Qual seu nome? ')
nome2 = input('Qual seu nome? ')
nome3 = input('Qual seu nome? ')
nome4 = input('Qual seu nome? ')
nome5 = input('Qual seu nome? ')

# Cria uma lista com os nomes 
lista = [nome, nome2, nome3, nome4, nome5]

# Sorteia um nome aleatorio da lista 
sorteado = random.choice(lista)

# Imprime o nome sorteado e adiciona um emoji 
print(emoji.emojize('O aluno sorteado foi {} :sunglasses:'.format(sorteado)))
