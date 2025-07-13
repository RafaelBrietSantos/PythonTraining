# Pede o nome ao usuário.
# .strip(): como já vimos, remove espaços extras no início e fim.
# .title(): capitaliza a primeira letra de cada palavra (Ex: "maria silva" vira "Maria Silva").
nome = input("Qual é o seu nome? ").strip().title()

print("Analisando seu nome...")

# .upper(): converte o nome para letras maiúsculas.
print("Seu nome em maiúsculas é: {}".format(nome.upper()))

# .lower(): converte o nome para letras minúsculas.
print("Seu nome em minúsculas é: {}".format(nome.lower()))

# .split(): divide a string em uma lista de strings, usando espaços como separador.
# Ex: se nome = "Maria Silva", 'nome_dividido' será ['Maria', 'Silva'].
nome_dividido = nome.split()

# len(nome_dividido[0]): Acessa o primeiro item da lista (o primeiro nome) e conta suas letras.
print("Seu primeiro nome tem {} letras".format(len(nome_dividido[0])))

# .join(lista): Junta os elementos de uma lista em uma única string.
# O "" (string vazia) antes do .join() significa que os elementos são unidos sem nada entre eles.
# Ex: se 'nome_dividido' = ['Maria', 'Silva'], 'nome_completo_sem_espacos' será "MariaSilva".
nome_completo_sem_espacos = "".join(nome_dividido)

# len(): conta o total de caracteres da string 'nome_completo_sem_espacos'.
print("Seu nome completo tem {} letras no total".format(len(nome_completo_sem_espacos)))
