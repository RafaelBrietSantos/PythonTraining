n = input('Digite algo: ') # Não precisa do str() aqui, input já retorna string por padrão

print('O tipo primitivo desse valor é ', type(n) )
print('Contém apenas espaços? ' , n.isspace())
print('Contém apenas números? ', n.isnumeric())
print('Contém apenas letras? ', n.isalpha())
print('É alfanumérico (letras e/ou números)? ', n.isalnum()) # Corrigido aqui!

''' Também pode explorar outros métodos úteis:
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada (primeira letra maiúscula e o resto minúscula)? ', n.istitle())'''