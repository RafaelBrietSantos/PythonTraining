i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
# Aqui é um ex do range e como ele funciona 
# Ele tem inicio, fim, e o passo q seria o tamanho do passo 
# O quanto ele "pula" 
for c in range(i, f+1, p):
    print(c)
print('FIM')

# Esse programa é otimo pra testar/entender o loop for 