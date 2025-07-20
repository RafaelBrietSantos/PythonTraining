

num = int(input('Digite um numero para a tabuada: '))
tab = int(input('Voce quer que a tabuada va ate que numero? '))

tab = tab + 1

num_tab = 0 

# 'ROUBEI' aqui pois nn ava conseguindo pensar um jeito pra farzer o 1 
# pois sempre dava ex 1 x 0 = 1
print(f' {num}  x  0 = 0')
for n in range(1, tab):
    num_tab += 1 
    calculo = num * num_tab
    print(f' {num}  X  {num_tab} = {calculo}')

