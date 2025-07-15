# Problema: Permitir que o usuário crie um arquivo de texto com um nome personalizado
# e escreva conteúdo nele, garantindo que o nome do arquivo seja dinamicamente gerado (ex: 'meu_documento.txt').

nome = input('Me dê o nome para o seu arquivo: ')

escreve = input('O nome do arquivo será: {} \nAgora digite o que você quer escrever nele: '.format(nome))

# A linha abaixo cria a string final para o nome do arquivo (ex: "meuarquivo.txt").
# É essencial que o nome do arquivo seja completo antes de ser passado para a função open().
arquivo_nome = '{}.txt'.format(nome)

# --- OPEN ---
# A função open() é utilizada para a abertura de arquivos.
# SINTAXE:
#         open('nome_do_arquivo.txt', 'modo')
# Modos de Abertura Comuns:
#     'w' (write): Abre o arquivo para escrita. Se o arquivo já existir, seu conteúdo é APAGADO.
#                  Se não existir, um novo arquivo é criado.
#     'r' (read): Abre o arquivo APENAS para leitura. Se o arquivo não existir, ocorre um erro.
#     'a' (append): Abre o arquivo para adição de conteúdo. Se o arquivo já existir, o novo
#                   conteúdo é ADICIONADO ao final do que já existe. Se não existir, um novo arquivo é criado.
#     'x' (exclusive creation): Cria um novo arquivo para escrita, mas SÓ SE o arquivo ainda não existir.
#                               Se o arquivo já existir, ocorre um erro.

'''
    ⚠️ Dica de Aprendizado: Problema comum com '.format()' ao definir o nome do arquivo!
    
    Eu tive um problema com essa parte de colocar o nome no arquivo através da entrada do usuário.
    Inicialmente, eu estava tentando fazer assim:
        arquivo = open ('{}.txt', 'w'.format(nome))

    O erro ocorria porque '.format(nome)' estava sendo aplicado APENAS à string do MODO ('w'),
    e não ao nome do arquivo. Isso fazia com que o Python tentasse criar um arquivo
    com o nome LITERAL '{}.txt', em vez de, por exemplo, 'meu_arquivo.txt'.

    A correção garante que a variável 'nome' seja inserida no nome do arquivo COMPLETO
    (ou seja, 'nome_do_arquivo.txt') ANTES de a função open() ser chamada.
'''
# Abre o arquivo com o nome personalizado fornecido pelo usuário, no modo de escrita ('w').
arquivo = open(arquivo_nome, 'w')

# Outra forma moderna e mais concisa de fazer o mesmo (usando f-strings):
# arquivo = open(f'{nome}.txt', 'w')


# --- WRITE ---
# O método write() é utilizado para gravar informações/conteúdo em um arquivo que já foi aberto.
# SINTAXE:
#     arquivo.write('o que você quer escrever')
arquivo.write(escreve)


# --- CLOSE ---
# O método close() é EXTREMAMENTE importante para encerrar o arquivo após as operações.
# Isso libera recursos do sistema e garante que todo o conteúdo seja salvo corretamente.
# SINTAXE:
#     arquivo.close()
arquivo.close()

print(f"Arquivo '{nome}.txt' criado e editado com sucesso!")