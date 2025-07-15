total_primos = 0 
# 'total_primos = 0'
# Esta variável é a sua "sacola" principal para contar quantos números primos foram encontrados no final.
# Ela começa em zero e só vai aumentar quando um número for confirmado como primo.

# 'for num in range(1, 101):'
# Este é o **primeiro loop (o loop "de fora")**.
# Ele vai testar CADA número de 1 a 100 (lembre-se que 'range(1, 101)' vai até 100).
# A variável 'num' vai ser cada um desses números que estamos verificando (1, 2, 3, ..., 100).
for num in range(1, 101):
    cont = 0 
    # 'cont = 0'
    # Esta variável é um **contador de divisores**.
    # Ela é "resetada" para zero a CADA NOVO 'num' que o loop de fora pega.
    # Isso é crucial! Para cada 'num', queremos começar a contar seus divisores do zero.
    
    # 'for n in range (1, num + 1):'
    # Este é o **segundo loop (o loop "de dentro")**.
    # Para cada 'num' (por exemplo, se 'num' for 7), este loop vai de 1 até o próprio 'num' (1 até 7).
    # A variável 'n' vai assumir cada valor nesse intervalo (1, 2, 3, 4, 5, 6, 7).
    for n in range (1, num + 1):
        # 'if num % n == 0:'
        # Dentro do loop de dentro, esta linha verifica se 'num' (o número que estamos testando)
        # é divisível por 'n' (o possível divisor atual).
        # Se 'num % n == 0', significa que 'n' é um divisor de 'num'.
        if num % n == 0:
            # 'cont += 1'
            # Se 'n' for um divisor, aumentamos o contador de divisores ('cont') em 1.
            cont += 1
            # Exemplo: Se 'num' é 7:
            #   - n=1: 7%1==0 -> cont=1
            #   - n=2: 7%2!=0
            #   - n=3: 7%3!=0
            #   - n=4: 7%4!=0
            #   - n=5: 7%5!=0
            #   - n=6: 7%6!=0
            #   - n=7: 7%7==0 -> cont=2 (final para o 7)

    # 'if cont == 2:'
    # Depois que o **loop de dentro termina** (ou seja, 'num' foi testado por todos os seus possíveis divisores),
    # verificamos o valor final de 'cont'.
    # Um número primo tem EXATAMENTE 2 divisores: 1 e ele mesmo.
    # Se 'cont' for igual a 2, significa que 'num' é um número primo.
    if cont == 2:
        # 'total_primos += 1'
        # Se 'num' for primo, adicionamos 1 à nossa "sacola" de números primos encontrados.
        total_primos += 1
        # Opcional: print(f"O número {num} é primo!") # Você poderia imprimir os primos aqui para ver quais são.
    
# 'print('Temos {} de numeros primos entre 1 a 100'.format(total_primos ))'
# Após o **loop de fora terminar** (ou seja, todos os números de 1 a 100 foram testados),
# o programa exibe o total de números primos que foram encontrados.
print('Temos {} de números primos entre 1 e 100.'.format(total_primos))
    
    