# Pede ao usuário o nome de uma cidade.
# .strip(): remove espaços extras no início e fim.
# .title(): capitaliza a primeira letra de cada palavra (Ex: "santo andre" vira "Santo Andre").
city = str(input("Digite o nome de uma cidade: ")).strip().title()

# Converte a cidade para minúsculas.
# Isso é crucial para que a verificação 'startswith("santo")' seja insensível a maiúsculas/minúsculas.
# Se a cidade original for "Santo André", 'cityf' será "santo andre".
cityf = city.lower()

# Verifica se a string 'cityf' (em minúsculas) começa com a palavra "santo".
# .startswith("prefixo"): é um método de string que retorna True se a string começar com o 'prefixo' dado, e False caso contrário.
palavra = cityf.startswith("santo")

# Você também pode fazer a verificação comparando um "slice" da string:
# print(city[:5] == "Santo")
# 'city[:5]' pega os primeiros 5 caracteres da string 'city' (que está capitalizada).
# Depois, compara se esses 5 caracteres são EXATAMENTE "Santo".
# Esta abordagem é menos flexível se você quiser ignorar a capitalização, a menos que você aplique .lower() também.

print("Analisando a cidade...")

# Imprime o resultado booleano (True ou False) da verificação.
# O 'True' significa que a cidade começa com "santo", 'False' que não.
print(palavra)

