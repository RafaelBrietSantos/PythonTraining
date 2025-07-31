from random import randint
print('Sou o seu computador...')
print('Acabei de pensar em um numero de 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
numero_pc = randint(0, 10)
print('Você tem apenas 3 chances.')
chance = 0
while  chance <= 2:
    chance += 1
    palpite = int(input('Qual é o seu palpite? '))
    if palpite ==  numero_pc:
        print('Parabens você acertou!!')
        break
    else:
        if palpite > numero_pc:
            print('Menos... Tente mais uma vez.')
            print(f'{chance}/3')
        elif palpite < numero_pc:
            print('Mais... tente outra vez.')
            print(f'{chance}/3')

if chance == 3:
    print('Não foi dessa vez mas ok...')
print('Obrigado por jogar.')

