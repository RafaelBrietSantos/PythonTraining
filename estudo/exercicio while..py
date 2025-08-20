nome = input('Digite seu nome: ') .title()
junta = nome.replace(' ', '')
print(nome)
print(junta)
quantidade_de_letras = len(junta) 
tamanho_nome = len(nome)

contador = 0
while contador is not tamanho_nome:
    
    letra = nome[contador]
    print(nome[contador], end= '*')
    contador += 1
    
print('\n')

print(f'Seu nome tem {quantidade_de_letras} letras')
     



