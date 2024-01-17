import procfit
import programare

import pandas as pd

import pyautogui
pyautogui.PAUSE = 0.5
import time


programare.programareloginAuto()
procfit.procfitLoginAuto()

while True:
    programare.programareSaveAuto()
    pyautogui.hotkey('alt', 'tab')
    time.sleep(3)
    procfit.procfitInsertPedidoAuto()
    pyautogui.hotkey('alt', 'tab')
        
    # Espera 5 minutos antes da próxima iteração
    time.sleep(300)  # 300 segundos = 5 minutos
