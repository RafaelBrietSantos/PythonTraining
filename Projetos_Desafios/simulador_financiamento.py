
casa = float(input ('Valor da casa: R$'))

salario = float(input('Seu salario: R$'))

anos = float(input('Quantos anos de financiamento? '))

fi = anos * 12  # meses

pres = casa / fi
yt = salario * 0.30
print('Para pagar a casa de R${:.2f} em {:.0f} anos a prestação sera de R${:.2f}'.format(casa, fi, pres), end=' ')
print('e 30% do seu salario é R${:.2f}'.format(yt)) 
if yt >= pres:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')


