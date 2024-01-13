import pandas as pd
from openpyxl import load_workbook

import pyautogui
pyautogui.PAUSE = 0.5
import time

planilha = pd.read_excel("pedidos.xlsx")

print(planilha.head())

# Simula pressionamento da tecla Win
pyautogui.hotkey('win')

pyautogui.write('progra')
pyautogui.write('mare')

time.sleep(0.2)

# # # Simula pressionamento da tecla tab
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')

# Simula pressionamento da tecla enter
pyautogui.hotkey('enter')

time.sleep(0.1)

# # Simula pressionamento da tecla tab
pyautogui.write('lucas rosa')
pyautogui.hotkey('tab')
pyautogui.write('lucas')

# # Simula pressionamento da tecla tab
pyautogui.hotkey('tab')

pyautogui.hotkey('enter')


# Simula pressionamento do botão de funçoes
pyautogui.moveTo(147, 601, 0.2)
pyautogui.click(147, 60)


#sequencia de tab até localizar a empresa que desejamos
pyautogui.hotkey('tab')

# Simula pressionamento do botão de pedidos aguardando separação
pyautogui.moveTo(147, 601, 0.2)
pyautogui.click(147, 60)

# Simula pressionamento do botão de salvar os pedidos na planilha
pyautogui.moveTo(147, 601, 0.2)
pyautogui.click(147, 60)


time.sleep(6)