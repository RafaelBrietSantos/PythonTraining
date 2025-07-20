import random
print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
print('O jogo funciona assim: ')
print('Você vai colocar digitar um entre Pedra/papel/tesoura')
print('E o computador vai escolher aleatoriamente entre Pedra/papel/tesoura')
print('Vamos ver quem ganha?')
print('-=' * 40)

placar = 0 #placar da Maquina
placar_user = 0 #placar do usuario 
while  placar <= 2 and placar_user <= 2: 
    user = input('Digite: ').strip().lower()
    lista = ['pedra', 'papel', 'tesoura']
    computador = random.choice(lista)
    print(f'O computador escolheu {computador}')

    if user == computador:
         print('\033[1;30mEmpate!\033[m')
         print('PLACAR {} X {}'.format(placar, placar_user))

         print('')
         print('-=' * 40)
         print('')

    elif (user == 'pedra' and computador == 'tesoura') or\
         (user == 'papel' and computador == 'pedra') or\
         (user == 'tesoura' and computador == 'papel'):
        placar +=1
        print ('\033[4;32mMais 1+ PONTO PRA VC ༼ つ ◕_◕ ༽つ!!\033[m')
        print('PLACAR {} X {}'.format(placar, placar_user))
        print('')
        print('-=' * 40)
        print('')

    else:
        placar_user +=1
        print ('\033[1;31mPonto da MAQUINA (T_T).\033[m')
        print('PLACAR {} X {}'.format(placar, placar_user))
        print('')
        print('-=' * 40)
        print('')

if placar_user == 3:
    print('\033[1;31m 💔 A MAQUINA VENCEU! (⌐■_■).\033[m')
else:
    print('\033[4;32m 🏆PARABENS VOCÊ VENCEU A MAQUINA!\033[m')

print('-=' * 40)
print('Obrigado por jogar!')

# --- ANOTAÇÃO IMPORTANTE SOBRE A CONDIÇÃO DO LOOP ---
#
# Minha dúvida principal na construção desse jogo foi a condição do 'while'.
#
# Objetivo: O jogo deve continuar ENQUANTO NENHUM DOS DOIS JOGADORES TIVER ATINGIDO 3 PONTOS.
#           O loop deve parar ASSIM QUE UM DOS JOGADORES CHEGAR A 3 PONTOS.
#
# Tentativas e Raciocínio:
#
# 1. Primeira tentativa: 'while placar <= 3 or placar_user <= 3:'
#    - Resultado: O código NÃO PARAVA!
#    - Por quê? A condição 'OR' (OU) significa que o loop continua se PELO MENOS UMA das condições for verdadeira.
#      Mesmo que um jogador chegasse a 3 pontos (ex: placar = 3), a condição 'placar <= 3' ainda seria VERDADEIRA.
#      Para o loop parar, AMBAS as condições teriam que ser FALSAS (ou seja, ambos os placares teriam que ser MAIORES que 3, tipo 4 ou mais), o que nunca aconteceria com o jogo de "primeiro a 3".
#
# 2. Segunda tentativa: 'while placar <= 3 and placar_user <= 3:'
#    - Resultado: O jogo ia ATÉ OS 4 PONTOS para o vencedor.
#    - Por quê? A condição 'AND' (E) significa que o loop continua APENAS SE AMBAS as condições forem verdadeiras.
#      Quando um jogador atingia 3 pontos (ex: placar = 3), a condição 'placar <= 3' AINDA ERA VERDADEIRA.
#      Então, o loop rodava mais uma vez. Somente se o placar passasse de 3 (chegasse a 4), a condição 'placar <= 3' se tornaria FALSA, e o loop pararia. Isso fazia o jogo ir além dos 3 pontos desejados.
#
# 3. Solução Atual (e correta para "primeiro a 3"): 'while placar <= 2 and placar_user <= 2:'
#    - Resultado: O jogo para EXATAMENTE quando um dos jogadores atinge 3 pontos.
#    - Por quê? Ao usar '<= 2', estamos dizendo: "Continue enquanto o placar do computador for 0, 1 ou 2 E o placar do usuário for 0, 1 ou 2".
#      Assim que um dos placares atinge 3, a condição correspondente (ex: 'placar <= 2') se torna FALSA.
#      Como é um 'AND', se uma parte é falsa, toda a condição se torna falsa, e o loop para.
#      Isso garante que o jogo termine na rodada em que alguém faz o terceiro ponto.
#
# Essa foi uma parte que exigiu bastante atenção à lógica booleana!
# --- FIM DA ANOTAÇÃO ---
