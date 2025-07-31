#       --- Tupla --- 
# ela é uma coleção codernada e imutavel de elementos 
# ela não muda de pois de declarada 

# tupla exemplo

minha_tupla = (1, 2, 2, 3, 4)

print(f'minha tupla:{minha_tupla}')

print(f'minha_tula[0]', minha_tupla[0])
print(f'minha_tula[2]', minha_tupla[2])
print(f'minha_tula[-1]', minha_tupla[-1]) # Mostra o ultimo 



# Cont
contagem = minha_tupla.count(2)
print('Quantidade de vezes que o eleento 2 aparece:', contagem )

indice = minha_tupla.index(3)
print('Indice da primeira ocorrencia de elementos 3:', indice)