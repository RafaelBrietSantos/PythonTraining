# Pedimos ao usuário para digitar algo e armazenamos na variável 'n'.
# O 'input()' já retorna uma string por padrão, então 'str()' é opcional aqui,
# mas não prejudica o funcionamento.
n = str(input('Digite algo: '))

# Usamos uma f-string (string formatada) para exibir várias informações de uma vez.
# As f-strings (f'...') permitem embutir variáveis e expressões diretamente dentro de chaves {}.
print(f'''
    É Alfanumérico? {n.isalnum()},     # Verifica se a string contém APENAS letras e/ou números.
                                        # Espaços e símbolos retornam False.

    É Alfabético? {n.isalpha()},       # Verifica se a string contém APENAS letras.
                                        # Números, espaços e símbolos retornam False.

    É Minúscula? {n.islower()},        # Verifica se TODOS os caracteres alfabéticos na string são minúsculos.
                                        # Caracteres não alfabéticos (como números ou símbolos) são ignorados.

    É Maiúscula? {n.isupper()},        # Verifica se TODOS os caracteres alfabéticos na string são maiúsculos.
                                        # Caracteres não alfabéticos são ignorados.

    Está Capitalizada? {n.istitle()},  # Verifica se a string é uma "palavra capitalizada" ou "título".
                                        # Ou seja, a primeira letra de CADA palavra é maiúscula e o resto é minúsculo.

    É Decimal? {n.isdecimal()},        # Verifica se a string contém APENAS dígitos que podem ser usados para um número decimal.
                                        # Diferente de 'isnumeric()', 'isdecimal()' é mais restrito (ex: não aceita frações Unicode).
                                        # Geralmente, para números inteiros, 'isnumeric()' ou 'isdigit()' são mais comuns.

    É Numérica? {n.isnumeric()},       # Verifica se a string contém APENAS caracteres numéricos (incluindo dígitos, expoentes, frações Unicode).
                                        # Mais abrangente que 'isdecimal()'. Para inteiros simples (0-9), funciona.

    É Espaço? {n.isspace()},           # Verifica se a string contém APENAS espaços em branco.

    Tipo: {type(n)}                     # Retorna o tipo de dado da variável 'n' (sempre <class 'str'> aqui).
      ''')