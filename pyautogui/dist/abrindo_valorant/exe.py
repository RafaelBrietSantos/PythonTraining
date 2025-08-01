import pyautogui as posicaoMaouse
import pyautogui as tempoEspera

def AbrindoClick():
    # Movendo mouse até o botão do windos
    '''posicaoMaouse.moveTo(25, 1062)'''

    #click na posição desejada 
    posicaoMaouse.click(25, 1062)

    # Tempo de espera para o pc possa pensar / processar as informaçoes 
    tempoEspera.sleep(0.5)

    '''# Movendo ate a cauculadora 
    posicaoMaouse.moveTo(473, 746)'''

    #clicando na calculadora 
    posicaoMaouse.click(473, 746)


    print(posicaoMaouse.position())



def AbrindoPesquisando():

    posicaoMaouse.click(72, 1055)
    tempoEspera.sleep(0.5)

    #Digita algo programado
    posicaoMaouse.typewrite('calc')
    tempoEspera.sleep(2)

    posicaoMaouse.click(607, 523)

def valorant():
    posicaoMaouse.click(-1642, 1061)
    tempoEspera.sleep(15)
    posicaoMaouse.click(237, 570)
    tempoEspera.sleep(2)
    posicaoMaouse.click(440, 392)
    tempoEspera.sleep(35)

    posicaoMaouse.click(140, 253)
    tempoEspera.sleep(1.5)
    posicaoMaouse.click(765, 81)
    tempoEspera.sleep(1.5)
    posicaoMaouse.click(776, 944)
valorant()
tempoEspera.sleep(3)
print(posicaoMaouse.position())