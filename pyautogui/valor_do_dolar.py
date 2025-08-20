import pyautogui as posicaoMouse
import pyautogui as tempoEspera 
import pyautogui as precione



posicaoMouse.click(73, 1065)
tempoEspera.sleep(1)
posicaoMouse.typewrite('Chrome')
tempoEspera.sleep(0.5)
posicaoMouse.click(197, 523)
tempoEspera.sleep(0.5)

# Escreve algo
posicaoMouse.typewrite('Valor do dolar hoje', interval=0.1)

# Precione ('tecla')
precione.press('enter')



'''posicaoMouse.click()'''

tempoEspera.sleep(3)


print(posicaoMouse.position())