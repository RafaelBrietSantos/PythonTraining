print('=' * 7)
print('10 TERMOS DE UMA PA')
print('=' * 7)
ter1 = int(input('Primeiro termo: '))
raz = int(input('Segundo termo: '))


termo = ter1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -->', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos voce quer mostrar a mais? '))
print('FIM')
        