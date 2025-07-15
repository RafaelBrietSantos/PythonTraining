print('=' * 7)
print('10 TERMOS DE UMA PA')
print('=' * 7)

# 'ter1 = int(input('primeiro termo: '))'
# Pede ao usuário o primeiro termo da Progressão Aritmética.
# O valor é convertido para um número inteiro e guardado em 'ter1'.
ter1 = int(input('Primeiro termo: '))

# 'raz = int(input('razão: '))'
# Pede ao usuário a razão da Progressão Aritmética.
# A razão é o valor constante que é adicionado a cada termo para obter o próximo.
# O valor é convertido para um número inteiro e guardado em 'raz'.
raz = int(input('Razão: '))

# 'deci = ter1 + (10 - 1) * raz'
# Esta linha calcula o **décimo termo** da PA.
# A fórmula geral para o n-ésimo termo de uma PA é: an = a1 + (n - 1) * r
# Onde:
# - 'an' é o termo que queremos encontrar (aqui, o 10º termo)
# - 'a1' é o primeiro termo ('ter1')
# - 'n' é a posição do termo (aqui, 10)
# - 'r' é a razão ('raz')
# Então, 'deci' = primeiro termo + (10 - 1) * razão.
deci = ter1 + (10 - 1) * raz

# 'for c in range(ter1, deci + raz, raz):'
# Este loop 'for' vai gerar e exibir os termos da PA.
# 'range()' funciona assim: (início, fim_exclusivo, passo)
# - 'ter1': O loop começa no primeiro termo fornecido.
# - 'deci + raz': O loop precisa ir *até e incluir* o décimo termo. Como `range()` exclui o último valor,
#   somamos a razão ('raz') ao décimo termo ('deci') para garantir que o décimo termo seja incluído.
# - 'raz': Este é o passo do `range()`. A cada iteração, ele adiciona a razão ao termo anterior,
#   gerando o próximo termo da PA.
# 'c' é a variável que recebe cada termo da PA gerado pelo `range()`.
for c in range(ter1, deci + raz, raz): 
    # 'print('{} '.format(c), end=' =>')'
    # Imprime o termo atual ('c') seguido de um espaço.
    # 'end=' =>'' faz com que o próximo termo seja impresso na mesma linha,
    # separado por ' =>'.
    print('{} '.format(c), end=' =>')
    
print('PRONTO') # Imprime "PRONTO" depois que todos os 10 termos foram exibidos.