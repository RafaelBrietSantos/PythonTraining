import pyautogui as mouse
import pyautogui as precione
import pyautogui as click
import pyautogui as digite

#preciona as teclas windos + r
precione.hotkey('win','r')
digite.write('notepad', interval=0.1)
precione.press('enter')
mouse.sleep(0.5)
digite.write('ola, mundo!', interval=0.1)
precione.hotkey('ctrl','s')
mouse.sleep(1)
digite.write('arquivo', interval=0.1)
mouse.sleep(0.5)
mouse.click(985, 844)



