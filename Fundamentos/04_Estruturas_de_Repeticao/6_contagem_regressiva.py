import time # type: ignore


# 'seg = time.sleep(1)'
# Esta linha tenta atribuir o resultado de 'time.sleep(1)' à variável 'seg'.
# 'time.sleep(1)' PAUSA a execução do programa por 1 segundo.
# No entanto, 'time.sleep()' NÃO RETORNA NENHUM VALOR. Ele apenas faz uma pausa.
# Por não retornar nada, o valor atribuído a 'seg' será 'None'.
# Embora não cause um erro aqui, 'seg' não será útil para o que você quer.
# Geralmente, 'time.sleep()' é usado diretamente sem atribuição a uma variável.
seg = time.sleep(1)

# Aqui temos um exemplo de contagem regressiva com loop for
for con in range (10, 0, -1):
    print(con)
    time.sleep(1)
# Eu tinha feito assim de primeira |print(time.sleep(1), (con))| porem 
# Ficava escrito assim None 1 None 2 ai tirei e vi que dava pra fazer como o
# Exemplo a cima                 
print('.............🧨BOMMMMM🧨.............')
print('.........✨FELIZ ANO NOVOO!!✨.......')
