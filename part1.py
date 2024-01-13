import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

import pyautogui
pyautogui.PAUSE = 1
import time


# Simula pressionamento da tecla Win
pyautogui.hotkey('win')

pyautogui.write('SistemaDeVe')

time.sleep(0.2)

# # Simula pressionamento da tecla tab
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')

# Simula pressionamento da tecla enter
pyautogui.hotkey('enter')

# # Simula pressionamento da tecla tab
# pyautogui.hotkey('tab')

# pyautogui.write('user')
# pyautogui.hotkey('tab')
# pyautogui.write('123')


time.sleep(6)