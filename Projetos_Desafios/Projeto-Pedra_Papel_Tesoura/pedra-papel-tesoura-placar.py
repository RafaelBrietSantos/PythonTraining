import random
print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
print('O jogo funciona assim: ')
print('Você vai colocar digitar um entre Pedra/papel/tesoura')
print('E o computador vai escolher aleatoriamente entre Pedra/papel/tesoura')
print('Vamos ver quem ganha?')
print('-=' * 40)

placar = 0
placar_user = 0 
while  placar <= 2 and placar_user <= 2: 
    user = input('Digite: ').strip().lower()
    lista = ['pedra', 'papel', 'tesoura']
    computador = random.choice(lista)
    print(f'O computador escolheu {computador}')

    if user == computador:
         print('\033[1;30mEmpate!\033[m')
         print('PLACAR {}/{}'.format(placar, placar_user))

         print('')
         print('-=' * 40)
         print('')

    elif (user == 'pedra' and computador == 'tesoura') or\
         (user == 'papel' and computador == 'pedra') or\
         (user == 'tesoura' and computador == 'papel'):
        placar +=1
        print ('\033[4;32mMais 1+ PONTO PRA VC ༼ つ ◕_◕ ༽つ!!\033[m')
        print('PLACAR {}/{}'.format(placar, placar_user))
        print('')
        print('-=' * 40)
        print('')

    else:
        placar_user +=1
        print ('\033[1;31mPonto da MAQUINA (T_T).\033[m')
        print('PLACAR {}/{}'.format(placar, placar_user))
        print('')
        print('-=' * 40)
        print('')

if placar_user == 3:
    print('\033[1;31mA MAQUINA VENCEU! (⌐■_■).\033[m')
else:
    print('\033[4;32mPARABENS VOCÊ VENCEU A MAQUINA!\033[m')


print('-=' * 40)
        
 



print('Obrigado por jogar!')
