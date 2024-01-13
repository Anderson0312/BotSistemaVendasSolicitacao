import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

import pyautogui
pyautogui.PAUSE = 0.5
import time

planilha = pd.read_excel("pedidos.xlsx")

print(planilha.head())

# Simula pressionamento da tecla Win
pyautogui.hotkey('win')

pyautogui.write('proc')
pyautogui.write('fit')

time.sleep(0.2)

# # # Simula pressionamento da tecla tab
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')

# Simula pressionamento da tecla enter
pyautogui.hotkey('enter')

time.sleep(0.1)

# # Simula pressionamento da tecla tab
pyautogui.hotkey('tab')
# # Simula pressionamento da tecla tab
pyautogui.hotkey('tab')

pyautogui.write('anderson moura')
pyautogui.hotkey('tab')
pyautogui.write('123456')

# # Simula pressionamento da tecla tab
pyautogui.hotkey('tab')

pyautogui.hotkey('enter')

# Simula pressionamento do botão de funçoes
pyautogui.moveTo(147, 601, 0.2)
pyautogui.click(147, 601)


# # Simula pressionamento da atalho para localizar a aba de atacado
pyautogui.write('atac')
pyautogui.hotkey('ctrl', 'backspace')

# # Simula pressionamento da atalho para localizar a aba de solicitação de pedido
pyautogui.write('solic')
pyautogui.hotkey('enter')

# # Simula pressionamento do comando de atalho para iniciar um novo formulario de solicitação de pedido
pyautogui.hotkey('ctrl', 'i')



# Iterar sobre os IDs e armazená-los em uma variável
for index, row in planilha.iterrows():
        id_selecionado = row['pedido']
        
        #insere o numero do produto para puxar os dados
        pyautogui.write(id_selecionado)
        
        # # Simula pressionamento da tecla tab até o input de transportadora
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        
         #insere o numero da transportadora para puxar os dados
        pyautogui.write('78056')
        pyautogui.hotkey('tab')
        
        # Simula pressionamento do botão de insirir produtos de acordo com o numeor do pedido
        pyautogui.moveTo(147, 601, 0.2)

        pyautogui.click(147, 601)
        
        time.sleep(0.5)
        
        # # Simula pressionamento da atalho para salvar o pedido
        pyautogui.hotkey('ctrl', 'g')
        
        time.sleep(1)
                
        # Simula pressionamento de solicitar a impressão do pedido
        pyautogui.moveTo(147, 601, 0.2)

        pyautogui.click(147, 601)
        
        time.sleep(1.5)
        
        # Simula pressionamento de solicitar a impressão do pedido
        pyautogui.moveTo(147, 601, 0.2)

        pyautogui.click(147, 601)
        
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')

        time.sleep(0.2)

        break # Remove essa linha se deseja percorrer todos os IDs
    

time.sleep(6)