# Pede o nome completo ao usuário.
# .strip(): remove espaços extras do início e do final.
# .title(): capitaliza a primeira letra de cada palavra (ex: "rafael briet" vira "Rafael Briet").
nome = str(input("Digite seu nome completo: ")).strip().title()

# Verifica se a substring "Briet" está presente no nome.
# Uma forma mais direta de usar o 'in' para verificar a presença de uma substring.
# O 'in' retorna True ou False.
# Nota: Você está usando '.format()' aqui, mas ele espera um valor para formatar.
# Se a intenção é só mostrar o resultado do 'in', podemos fazer de forma mais simples.
# Exemplo do que você tentou: print("seu nome tem Briet?".format('Briet' in nome.lower()))
# O resultado de 'Briet' in nome.lower() (True ou False) não é formatado na string literal.
# Para mostrar o resultado do booleano diretamente, a f-string é mais clara:
# print(f"Seu nome tem 'Briet'? {'Briet' in nome}") # Verifica 'Briet' com a capitalização do .title()
# Ou, para garantir que a comparação seja sem distinção de maiúsculas/minúsculas:
# print(f"Seu nome tem 'briet' (ignorando maiúsculas/minúsculas)? {'briet' in nome.lower()}")


# --- Estrutura Condicional (if/else) ---
# Aqui, verificamos se a string "Briet" (com B maiúsculo, devido ao .title() na entrada)
# está presente na variável 'nome'.
if "Briet" in nome:
    print("Simmm, seu nome contém 'Briet'!") # Executa se a condição for verdadeira.
else:
    print("Nãooo, seu nome não contém 'Briet'!") # Executa se a condição for falsa.

# Uma forma mais robusta de fazer a verificação, ignorando maiúsculas e minúsculas:
# if "briet" in nome.lower(): # Converte o 'nome' para minúsculas antes de verificar.
#     print("Simm! Encontrei 'briet' no seu nome (ignorando maiúsculas/minúsculas).")
# else:
#     print("Não encontrei 'briet' no seu nome (ignorando maiúsculas/minúsculas).")