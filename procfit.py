import pandas as pd

import pyautogui
pyautogui.PAUSE = 1
import time


#para pegarmos a localização de onde queremos clicar
#print(pyautogui.position())

def procfitLoginAuto(): 
        # Simula pressionamento da tecla Win
        pyautogui.hotkey('win')

        pyautogui.write('proc') 
        pyautogui.write('fi')

        time.sleep(0.3)

        # Simula pressionamento da tecla enter
        pyautogui.hotkey('enter')

        time.sleep(4)

        # Simula pressionamento da tecla tab
        pyautogui.hotkey('tab')
        # Simula pressionamento da tecla tab

        time.sleep(0.5)

        pyautogui.write('anderson moura')
        pyautogui.hotkey('tab')
        pyautogui.write('123456')

        # # Simula pressionamento da tecla tab
        pyautogui.hotkey('tab')

        pyautogui.hotkey('enter')

        time.sleep(0.5)


        # Simula pressionamento do botão de funçoes
        pyautogui.moveTo(72, 137, 0.2)
        pyautogui.click(72, 137)

        time.sleep(0.5)

        # # Simula pressionamento da atalho para localizar a aba de atacado
        pyautogui.write('ro')
        pyautogui.hotkey('down')

        time.sleep(0.3)

        pyautogui.hotkey('enter')

        time.sleep(0.5)

        # # Simula pressionamento do comando de atalho para iniciar um novo formulariofi
        pyautogui.hotkey('ctrl', 'i')

        time.sleep(0.5)


def procfitInsertPedidoAuto():
        
        planilha = pd.read_csv('pedidos.csv', sep=';', encoding='iso-8859-1')
        # Iterar sobre os IDs e armazená-los em uma variável
        for index, row in planilha.iterrows():
                id_selecionado = int(row['Externo'])
                
                numpedidoStr = str(id_selecionado)
                
                #insere o numero do produto para puxar os dados
                pyautogui.write(numpedidoStr)
                
                # # Simula pressionamento da tecla tab até o input de transportadora
                pyautogui.hotkey('tab')
                time.sleep(0.2)
                
                #insere o numero da transportadora para puxar os dados
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.write('81749')
                pyautogui.hotkey('tab')
                
                # Simula pressionamento do botão de insirir produtos de acordo com o numeor do pedido
                pyautogui.moveTo(220, 163, 0.2)

                pyautogui.click(220, 163)
                
                time.sleep(0.5)
                
                # # Simula pressionamento da atalho para salvar o pedido
                pyautogui.hotkey('ctrl', 'g')
                
                time.sleep(2.5)
                        
                # Simula pressionamento de solicitar a impressão do pedido
                pyautogui.moveTo(824, 162, 0.2)

                pyautogui.click(824, 162)
                
                time.sleep(6.5)
                
                
                # Simula pressionamento de solicitar a impressão do pedido
                pyautogui.moveTo(222, 89, 0.2)

                pyautogui.click(222, 89)

                time.sleep(0.2)
                
                pyautogui.hotkey('enter')

                time.sleep(0.2)
                pyautogui.hotkey('enter')

                time.sleep(0.3)

                # # Simula pressionamento da atalho para fechar a aba aberta
                pyautogui.hotkey('ctrl', 's')

                time.sleep(2)
                # Remove essa linha se deseja percorrer todos os IDs

                # # Simula pressionamento do comando de atalho para iniciar um novo formulario de solicitação de pedido
                pyautogui.hotkey('ctrl', 'i')

                time.sleep(0.3)





