import time # Importei esse modulo 'time' para pegar o ano atual da maquina 

print('_=' * 20)
print('alistamento militar')

# Utilizeio o '.title()' para deixar a primeira letra em maiúsculo 
# Também faço o uso do '.strip()' para tirar espaços extras 
sexo = str(input('Qual o seu sexo? (Masculino/Feminino):  ')).strip().title()

'''aqui eu fiquei meio que sem saber o que fazer, pois pensei que mesmo deixando o if e o elif ali eu pensei que a parte do masculino também
ia continuar aparecendo aí comecei a quebrar muito minha cabeça mas agora está tranquilo pois entendi agora'''
if sexo == 'Feminino': # Correção: Usei 'Feminino' com 'F' maiúsculo para combinar com .title()
    print('Você não precisa se alistar.')
'''Meu erro estava sendo que o elif aqui estava apenas assim:
    elif: e tinha que estar assim elif sexo == masculino'''
# A linha abaixo (e o seu conteúdo) DEVE ESTAR ALINHADA com o 'if' acima.
elif sexo == 'Masculino': 
    ano = int(input('Digite o ano de nascimento: '))
    ano_atual = time.localtime().tm_year
    idade = ano_atual - ano
    # A linha abaixo foi o seu principal erro. Já pegamos o sexo lá em cima.
    # Remover ou comentar a linha: sexo = str(print('Qual o seu sexo?')) 

    if idade == 18:
        print ('Você tem {}, então já está na hora de se alistar'.format (idade))
    elif idade > 18:
        saldo = idade - 18
        ano_alis = ano_atual - saldo
        print ('Já passou da hora de você se alistar, você tem {}. Você deveria ter se alistado há {} ano(s) em {}.'.format (idade, saldo, ano_alis))
    
    elif idade < 18:
        saldo = 18 - idade
        ano_alis = saldo + ano_atual
        print('Você com {} não tem idade ainda para se alistar, faltam {} ano(s). Será em {}.'.format (idade, saldo, ano_alis))
# A linha abaixo (e o seu conteúdo) DEVE ESTAR ALINHADA com o 'if' e 'elif' acima.
else: # Adicionei um 'else' final para tratar sexos diferentes de Masculino/Feminino
    print('Opção de sexo inválida. Por favor, digite "Masculino" ou "Feminino".')

print('_=' * 20)

 '''to a muito tempo aqui e não consegui entender o meu erro ainda 
 elif sexo == 'Masculino': 
    ^^^^                       # SO FICA NESSE ERRO 
SyntaxError: invalid syntax

   '''


    
    