# Primeira vez utilizando o for

# ---- RESUMO BREVE DE COMO ELE FUNCIONA ----
# 1 - 'c' é a variável que usamos para representar cada valor do loop (pode ter qualquer nome)
# 2 - A função range(0, 51, 2) funciona assim:
#     2.1 - O 0 indica o valor inicial do loop (vai começar do 0)
#     2.2 - O 51 é o valor final, MAS o loop vai até o 50, porque o valor final nunca é incluído
#     2.3 - O 2 indica o passo, ou seja, vai contar de 2 em 2

for c in range(0, 51, 2):
    print(c, end=' ')

print('Acabou')

# Observação: o end=' ' faz com que os números sejam impressos na mesma linha,
# separados por um espaço, ao invés de um em cada linha.

