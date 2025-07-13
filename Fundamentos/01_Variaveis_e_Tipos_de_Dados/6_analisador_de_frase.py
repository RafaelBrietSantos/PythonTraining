# Pede uma frase ao usuário.
# .strip(): remove espaços extras no início e fim.
# .lower(): converte toda a frase para minúsculas. Isso é crucial para que a busca
#           (com count, find, rfind) não diferencie maiúsculas de minúsculas.
fra = str(input("Digite uma frase: ")).strip().lower()

# Pede a letra que o usuário deseja buscar na frase.
# .strip() e .lower() aqui também garantem a consistência na busca.
letra = str(input("Digite uma letra que deseja: ")).strip().lower()

# Confirma a letra que será buscada.
print("A letra que você escolheu é: {}".format(letra))

# .count(substring): Conta quantas vezes a 'letra' aparece na 'fra' (frase).
# Como já convertemos tudo para minúsculas, a contagem é precisa.
print("Ela aparece {} vezes na frase.".format(fra.count(letra)))

# .find(substring): Retorna a posição (índice) da PRIMEIRA ocorrência da 'letra'.
# Se a letra não for encontrada, retorna -1.
# Adicionamos +1 porque, como você notou, Python conta posições a partir do 0 (zero).
print('A primeira vez que "{}" aparece é na posição {}'.format(letra, fra.find(letra) + 1))

# .rfind(substring): Retorna a posição (índice) da ÚLTIMA ocorrência da 'letra'.
# Se a letra não for encontrada, retorna -1.
# Também adicionamos +1 para a posição "humana".
print('A última vez que "{}" aparece é na posição {}'.format(letra, fra.rfind(letra) + 1))

# Sua anotação no código é perfeita:
# # rfind retorna a posição da última ocorrência de uma letra
# # +1 porque o find começa do 0
