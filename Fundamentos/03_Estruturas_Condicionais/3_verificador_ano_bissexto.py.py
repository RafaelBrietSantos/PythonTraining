# Importa o módulo 'datetime', que permite trabalhar com datas e horas.
# Especificamente, importamos 'date' para pegar a data atual.
from datetime import date

# Pede ao usuário para digitar um ano.
# 'int()' converte a entrada para um número inteiro.
ano = int(input('Digite um ano que quer analisar (ou 0 para o ano atual): '))

# Verifica se o usuário digitou 0.
# Se sim, significa que ele quer analisar o ano atual.
if ano == 0:
     # 'date.today().year' obtém o ano atual do sistema.
    ano = date.today(). year

#   Lógica para verificar se o ano é bissexto 
# Um ano é bissexto se:
# 1. É divisível por 4 (ano % 4 == 0) E
# 2. NÃO é divisível por 100 (ano % 100 != 0) OU
# 3. É divisível por 400 (ano % 400 == 0)
# Os parênteses na condição '(ano % 4 == 0 and ano % 100 != 0)' são importantes
# para garantir que a lógica 'E' seja avaliada antes do 'OU'.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é bissexto'.format (ano))
else:
    print('O ano {} não é bissexto'.format (ano))
 