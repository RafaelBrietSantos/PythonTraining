#A função print é uma função que recebe o parametro
#que digitamos e imprime o resultado na tela
print("Exemplo 1 de função")

print("\n")

#Uma função
def minhaPrimeiraFuncao():
    print("Essa é a minha primeira função criada com Python")

minhaPrimeiraFuncao()

#-----------------------------------

def funcaoTexto(nome):
    print(nome, "Santos")

funcaoTexto("Ana")
funcaoTexto("Roger")
funcaoTexto("Marcos")

#-----------------------------------

print("\n\n")

def funcaoSaudacao(saudacao, nome):
    print(saudacao, nome)

funcaoSaudacao("Boa noite", "Ana")
funcaoSaudacao("Bom dia", "Cesar")
funcaoSaudacao("Boa tarde", "Luiza")

#-----------------------------------

print("\n\n")

#Funcao com 2 argumentos
def funcaoComArgumentos(nome, sobrenome):
    print("Nome completo:", nome,sobrenome)

nomeInput = input("Digite o seu nome: ")
sobrenomeInput = input("Digite o seu sobrenome: ")

funcaoComArgumentos(nomeInput, sobrenomeInput)
