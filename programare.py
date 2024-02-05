
import pyautogui
pyautogui.PAUSE = 1
import time

def programareloginAuto(login, password):
    # Simula pressionamento da tecla Win
    pyautogui.hotkey('win')

    pyautogui.write('progra')  
    pyautogui.write('mare.bat')
    time.sleep(0.3)

    # Simula pressionamento da tecla enter
    pyautogui.hotkey('enter')

    time.sleep(18)

    # # Simula pressionamento da tecla tab
    pyautogui.write(login)
    pyautogui.hotkey('tab')
    pyautogui.write(password)

    #Simula pressionamento da tecla tab
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')

    # Simula pressionamento do botão de funçoes do programare
    pyautogui.moveTo(927, 225, 0.2)
    pyautogui.click(927, 225)


def programareSaveAuto():
    # Simula pressionamento do botão data de alteração
    pyautogui.moveTo(36, 154, 0.2)
    pyautogui.click(36, 154)
    
    # Simula pressionamento do botão de filia da empresa
    pyautogui.moveTo(998, 131, 0.2)
    pyautogui.click(998, 131)

    # Simula pressionamento de escolher a filial HOSPINOVA
    pyautogui.moveTo(931, 157, 0.2)
    pyautogui.click(931, 157)

    # Simula pressionamento do botão de Atualiazar pedidos
    pyautogui.moveTo(528, 137, 0.2)
    pyautogui.click(528, 137)


    # Simula pressionamento do botão de Pedidos que estão aguardando separação
    pyautogui.moveTo(496, 291, 0.2)
    pyautogui.click(496, 291)

    # Simula pressionamento do botão Exportar arquivo .CSV
    pyautogui.moveTo(1011, 57, 0.2)
    pyautogui.click(1011, 57)

    # Simula pressionamento do botão para salvar o arquivo
    pyautogui.moveTo(80, 138, 0.2)
    pyautogui.click(80, 138)


    pyautogui.hotkey('enter')

    #Simula pressionamento da tecla tab
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')