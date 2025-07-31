'''def ProvaAluno(nota1, nota2, nota3):
    if resposta == 1:
        print('O aluno tirou', nota1)
    elif resposta == 2:
        print('O aluno tirou', nota2)
    elif resposta == 3:
        print('O aluno tirou', nota3)

resposta = int(input('Qual a prova vc quer saber sua nota? '))


ProvaAluno(nota1=9, nota2=7, nota3=8)'''

numeros = [10, 8, 8, 9, 10]
def calcula_media(numeros):
    
    soma_das_notas = sum(numeros)
    quantidade_de_notas = len(numeros)
    return soma_das_notas / quantidade_de_notas

media = calcula_media(numeros)
print(media)