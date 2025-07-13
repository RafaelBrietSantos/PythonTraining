sal = int(input ('Qual é o salario do funcionario? R$'))


# Verifica se o salário atual é MAIOR OU IGUAL a R$ 1250.
if sal >= 1250 :
    # Se o salário for R$ 1250 ou mais, o aumento é de 10% (0.1).
    # O novo salário ('aumento') é o salário original + 10% dele.
    aum = sal * 0.1 + sal
else:
    # Se o salário for MENOR que R$ 1250, o aumento é de 15% (0.15).
    # O novo salário é o salário original + 15% dele.
    aum = sal * 0.15 + sal
    
print('Quem ganhava {} passa a ganhar {}'. format (sal, aum))