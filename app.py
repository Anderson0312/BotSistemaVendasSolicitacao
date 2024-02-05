import procfit
import programare

import pyautogui
pyautogui.PAUSE = 1
import time

#-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=
# Somente solicita os pedidos, precisa ter a planilha atualizada com os dados do aguardando separaçaõ

pyautogui.hotkey('alt', 'tab')
procfit.procfitInsertPedidoAuto()

#-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=

# Faz todo o processo do zero, parte de solicitar pedido e atualizar a planilha com os dados necessarios

# programare.programareloginAuto('lucas rosa', 'lucas')
# procfit.procfitLoginAuto('anderson moura', '123456')
# pyautogui.hotkey('alt', 'tab')  

# while True: 
#     programare.programareSaveAuto()
#     pyautogui.hotkey('alt', 'tab')  
#     time.sleep(3)   
#     procfit.procfitInsertPedidoAuto()
#     # Espera 5 minutos antes da próxima iteração
#     time.sleep(10)  # 300 segundos = 6 minutos
#     pyautogui.hotkey('alt', 'tab')
#     pyautogui.hotkey('tab')
#     pyautogui.hotkey('enter')