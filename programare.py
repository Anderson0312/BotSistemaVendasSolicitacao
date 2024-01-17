import pyautogui
pyautogui.PAUSE = 0.5
import time

def programareloginAuto():
    # Simula pressionamento da tecla Win
    pyautogui.hotkey('win')

    pyautogui.write('progra')
    pyautogui.write('mare.bat')
    time.sleep(0.3)

    # Simula pressionamento da tecla enter
    pyautogui.hotkey('enter')

    time.sleep(13)

    # # Simula pressionamento da tecla tab
    pyautogui.write('lucas rosa')
    pyautogui.hotkey('tab')
    pyautogui.write('lucas')

    #Simula pressionamento da tecla tab
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(927, 225, 0.2)
    pyautogui.click(927, 225)

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(36, 154, 0.2)
    pyautogui.click(36, 154)

def programareSaveAuto():
    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(998, 131, 0.2)
    pyautogui.click(998, 131)

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(931, 157, 0.2)
    pyautogui.click(931, 157)

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(490, 308, 0.2)
    pyautogui.click(490, 308)

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(1011, 57, 0.2)
    pyautogui.click(1011, 57)

    # Simula pressionamento do botão de funçoes
    pyautogui.moveTo(73, 118, 0.2)
    pyautogui.click(73, 118)

    pyautogui.hotkey('enter')

    #Simula pressionamento da tecla tab
    pyautogui.hotkey('tab')
