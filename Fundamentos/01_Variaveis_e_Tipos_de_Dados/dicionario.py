pessoa = {'nome': 'Rafael', 'idade': 30, 'cidade': 'São Paulo'}

# Acessando valores por chave
print('nome', pessoa['nome'])
print('idade:', pessoa['idade'])
print('cidade', pessoa['cidade'])

# Se quiser adicionar algo a mais mesmo depois do dicionario ja declado:
pessoa['sobrenome'] = 'Briet'
print('sobrenome', pessoa['sobrenome']) 
print('meu dicionario:', pessoa)
# Remover 
del pessoa['sobrenome']
print('meu dicionario:', pessoa)

# Keys
chaves = pessoa.keys()
print(f'minhas chaves {chaves}')
print(f'Primeira chave', chaves[0] )

# Valores
valores = list(pessoa.values())
print('Valores do dicionario', valores)
print(f'Primeiro valor do dicionario: {valores[0]}')

itens = pessoa.items()
