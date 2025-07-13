import random 

# Imprime linhas pra decorar o início do jogo
print('-=---=-' * 10 )
print ('pensando em um numero de 0 a 5...')
print('-=---=-' * 10 )

# Gera um número inteiro aleatório entre 0 e 5 (inclusive)
# Este é o número secreto que o jogador deve adivinhar
num = random.randint(0,5)

res = int(input('Pode adivinhar qual é o numero? '))
print('Processando...')
print('-=---=-' * 10 )

# --- Primeira Tentativa ---
# Compara a resposta do usuário com o número gerado.
if res == num:
    print('Você é bom mesmo em ACERTOU EM CHEIO!!')
else:
    print('Não foi dessa vez tente novamente ')
    print('-=---=-' * 10 )
    s = int(input('responde: '))
    print('-=---=-' * 10 )
     # --- Segunda Tentativa ---
    # Pede uma nova resposta.
    if s == num:
        print('agora SIMM! ACERTOUUU!')
    else: 
        print('Caraca ta dificil em, tente novamente')
        print('-=---=-' * 10 )
        j = int(input('responde: '))
        print('-=---=-' * 10 )
        # --- Terceira e Última Tentativa ---
        # Pede a última resposta.
        if j == num:
            print('Ufaaaaaaaa!!, AGORA SIMMM!')
            print('-=---=-' * 10 )
        else:
            print('Poxa, não foi dessa vez, o numero era {}'.format(num))
            print('-=---=-' * 10 )
print('Fim do jogo')
