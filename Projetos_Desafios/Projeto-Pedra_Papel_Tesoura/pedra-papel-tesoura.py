import random
print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
print('O jogo funciona assim: ')
print('Você vai colocar digitar um entre Pedra/papel/tesoura')
print('E o computador vai escolher aleatoriamente entre Pedra/papel/tesoura')
print('Vamos ver quem ganha?')
print('-=' * 20)

user = input('Digite: ').strip().lower()
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print(f'O computador escolheu {computador}')
if user == computador:
    print('\033[1;30mEmpate!\033[m')
elif (user == 'pedra' and computador == 'tesoura') or\
     (user == 'papel' and computador == 'pedra') or\
     (user == 'tesoura' and computador == 'papel'):

    print ('\033[4;32mPARABENS VOCÊ GANHOU!!\033[m')
else:
    print ('\033[1;31mDerrota.\033[m')
print('-=' * 20)
print('Obrigado por jogar!')
