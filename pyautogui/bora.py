import pyautogui as escolha_opicao
import pyautogui as posicaoMaouse
import pyautogui as tempoEspera
import pyautogui as precione



opcao = escolha_opicao.confirm('Clique no botão desejado', 
              buttons=['valorant', 'youtube', 'faculdade', 'spotify'])


if opcao == 'valorant':

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

if opcao == 'youtube':

    posicaoMaouse.doubleClick(-1659, 440)
    tempoEspera.sleep(1)
    posicaoMaouse.click(-90, 67)
    precione.write('https://www.youtube.com/', interval=0.1)
    tempoEspera.sleep(0.5)
    precione.press('enter')




if opcao == 'faculdade':

    posicaoMaouse.doubleClick(-1659, 440)
    tempoEspera.sleep(1)
    posicaoMaouse.click(-90, 67)
    tempoEspera.sleep(1)
    posicaoMaouse.click(-237, 570)
    tempoEspera.sleep(1)
    posicaoMaouse.click(-1485, 98)
    tempoEspera.sleep(4)
    posicaoMaouse.click(-729, 528)
    tempoEspera.sleep(18)
    posicaoMaouse.click(-755, 367)
    tempoEspera.sleep(4)
    posicaoMaouse.doubleClick(-584, 128)
    posicaoMaouse.doubleClick(-584, 128)
    posicaoMaouse.doubleClick(-584, 128)

 
if opcao == 'spotify':

    posicaoMaouse.doubleClick(-1659, 440)
    tempoEspera.sleep(1)
    posicaoMaouse.click(-90, 67)
    precione.write('https://open.spotify.com/intl-pt', interval=0.1)
    tempoEspera.sleep(0.5)
    precione.press('enter')

