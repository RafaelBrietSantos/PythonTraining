num = int(input('Digite um número: '))
# 'num' é o limite superior que o usuário quer verificar.

print(f'\nAnalisando números de 1 até {num} para encontrar os primos:\n')

# O loop 'n' é o principal. Ele vai pegar CADA NÚMERO, de 1 até 'num', para testar se é primo.
for n in range(1, num + 1):
    cont = 0 
    # 'cont' é o contador de divisores. Ele ZERA para cada novo número 'n' que estamos testando.

    # O loop 'c' vai testar os divisores do número ATUAL 'n'.
    # Ele precisa ir de 1 até o próprio 'n' (por isso 'n + 1').
    for c in range (1, n + 1): # AQUI ESTAVA O AJUSTE PRINCIPAL: 'n + 1' ao invés de 'num + 1'
        # Se 'n' for divisível por 'c' (resto da divisão é zero).
        if n % c == 0:
            cont += 1 # Aumenta o contador de divisores.

    # Após verificar TODOS os possíveis divisores de 'n':
    # Se 'cont' for exatamente 2, significa que 'n' tem apenas 2 divisores (1 e ele mesmo), logo é primo.
    if cont == 2:
        # Imprime o número 'n' (que é o primo encontrado) em negrito.
        print(f'\033[1m{n}\033[m É PRIMO!') 
    # Se 'cont' não for 2, significa que 'n' não é primo.
    else:
        # Imprime o número 'n' e informa que não é primo.
        print(f'{n} NÃO é primo.')

print('\nAnálise concluída.')

    
    