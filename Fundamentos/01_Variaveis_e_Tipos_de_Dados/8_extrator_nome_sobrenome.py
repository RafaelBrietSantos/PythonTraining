# Pede o nome completo do usuário.
# .strip(): remove espaços extras do início e do final.
# .title(): capitaliza a primeira letra de cada palavra (ex: "maria silva" vira "Maria Silva").
# .split(): divide a string em uma lista de strings, usando espaços como separador.
#           Assim, se o usuário digitar "Rafael Briet", 'nom' se tornará ['Rafael', 'Briet'].

nom = str(input ('Digite seu nome completo: ')).strip().title().split()

print('Prazer em te conhecer!')

# Acessa o primeiro elemento da lista 'nom'.
# Como Python começa a contagem em 0, 'nom[0]' sempre será o primeiro nome.
print('Seu primeironome é {}'.format (nom [0]))

# Acessa o último elemento da lista 'nom'.
# Em Python, índices negativos contam a partir do final da lista.
# '-1' sempre se refere ao último elemento.
# Se a lista é ['Rafael', 'Briet'], 'nom[-1]' será 'Briet'.
print('Seu ultimo nome é {}'.format (nom [-1]))