tarefas = []

def adicionar_tarfa(tarefas, nome_tarefa):
    tarefa = {'nome': nome_tarefa, 'completada': False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} foi adicionado com sucesso!')
    return

def ver_tarefas(tarefas):
    print('\nLista de tarefas:')
    for indice, tarefa_atual in enumerate(tarefas, start=1):
        status = '✔️ ' if tarefa_atual['completada'] else ' '
        nome_tarefa = tarefa_atual['nome']
        print(f'{indice}. [{status}] {nome_tarefa}')
    return


def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1

    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['nome'] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else:
        print('Indice invalido.')
    return

def completar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1

    tarefas[indice_tarefa_ajustado]['completada'] = True
    print(f'Tarefa {indice} marcada como completada')
    return


def deletar_tarefa(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa['completada']]
    print('Tarefas completadas foram deletadas.')
    return


while True:

    print('\nMenu do Gerenciador de tarefas: ')
    print('1. Adicionar tarefa')
    print('2. Ver tarefas')
    print('3. Atuliazar tarefas ')
    print('4. Completar tarefas')
    print('5. Deletar tarefas completadas')
    print('6. Sair')

    escolha = input('Digite a sua escolha: ')

    if escolha == '1':
        nome_tarefa = input('Nome da tarefa que deseja adicionar: ')
        adicionar_tarfa(tarefas, nome_tarefa)
    elif escolha == '2':
        ver_tarefas(tarefas)
    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = int(input('Digite o numero da tarefa que deseja atualizar: '))
        novo_nome = input('Digite o novo nome da tarefa: ')
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = int(input('Qual tarefa você deseja completar:'))
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == '5':
        deletar_tarefa(tarefas)
        ver_tarefas(tarefas)

    elif escolha == '6':
        break

print('Programa finalizado (☞ﾟヮﾟ)☞')