#era apenas para conseguir ler o arquivo porem tive uma ideia de me desafiar e acabei fazendo isso ai 
#foi ate que divertido me aventurar aqui ksksksksks

nome = input('Digite seu nome: ').strip() .title() 
quantas = int(input('Pessoas mora com você? '))


if quantas > 1:
    trabalha = input('Das pessoas que mora com vc so vc trabalha?')
    if trabalha == 'não':
        trabalha_num = int(input('Quantaa pessoas contando com vc tem uma renda?'))
        if trabalha_num >= 0  :
          salario = float(input('Mede a renda total de vocêS: '))
    # ponto de atenção pra mim é q eu não tava conseguindo pensar a onde esse
    # else deveria ficar pra nn ficar sem chance de conseguir a vareavel salario 
    #tanto q ele tava la atras 
# else: <-- aqui 

    else: 
        salario = float(input('Qual o seu salario: '))

print('')
print('_=_' * 30)
print('')

renda_per_capita =  salario  /  quantas
print(f'A renda percapita da sua familia é de {renda_per_capita }')
arquivo = open(f'{nome}_renda_per_capita.txt', 'x')
arquivo.write(f'Nome: {nome} \nQuantas pessoas moram com ele: {quantas} \nQuantas delas trabalham: {trabalha} \nSalario: {salario} \nRenda per capita: {renda_per_capita}')
arquivo.close()
# ----- LEITURA DO ARQUIVO -----
#  -Essa era a parte da aula-
print ('O seu documento ficou da seguinte forma:')
leitura = open(f'{nome}_renda_per_capita.txt', 'r')
print(leitura.read())
leitura.close()

