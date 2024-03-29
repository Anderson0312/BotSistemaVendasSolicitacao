import pandas as pd

import pyautogui
pyautogui.PAUSE = 1
import time


# para pegarmos a localização de onde queremos clicar
#print(pyautogui.position())

def procfitLoginAuto(login, password): 
        # Simula pressionamento da tecla Win
        pyautogui.hotkey('win')

        pyautogui.write('proc') 
        pyautogui.write('fi')

        time.sleep(0.4)

        # Simula pressionamento da tecla enter
        pyautogui.hotkey('enter')

        time.sleep(7)

        # Simula pressionamento da tecla tab
        pyautogui.hotkey('tab')
        # Simula pressionamento da tecla tab

        time.sleep(1)

        pyautogui.write(login)
        pyautogui.hotkey('tab')
        pyautogui.write(password)

        # # Simula pressionamento da tecla tab
        pyautogui.hotkey('tab')

        pyautogui.hotkey('enter')

        time.sleep(1)


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
        
        numero_de_linhas = len(planilha)
        # Iterar sobre os IDs e armazená-los em uma variável
        for index, row in planilha.iterrows():
                if numero_de_linhas == 1:
                        print('Planilha de pedido vazia')
                        break
                else:
                        id_selecionado = row['Externo']
                        
                        numpedidoStr = str(id_selecionado)
                        pedidoFiltrado = numpedidoStr[:-2]
                        #insere o numero do produto para puxar os dados
                        pyautogui.write(pedidoFiltrado)
                        #print(pedidoFiltrado)
                        
                        # # Simula pressionamento da tecla tab até o input de transportadora
                        pyautogui.hotkey('tab')
                        time.sleep(0.2)
                        
                        #insere o numero da transportadora para puxar os dados
                        pyautogui.moveTo(321, 423, 0.2)

                        pyautogui.click(321, 423)

                        time.sleep(0.2)
                        
                        # Simula pressionamento do botão de insirir produtos de acordo com o numeor do pedido
                        pyautogui.moveTo(220, 163, 0.2)

                        pyautogui.click(220, 163)
                        
                        time.sleep(0.7)
                        
                        # # Simula pressionamento da atalho para salvar o pedido
                        pyautogui.hotkey('ctrl', 'g')
                        
                        time.sleep(3)
                                
                        # Simula pressionamento de solicitar a impressão do pedido
                        pyautogui.moveTo(824, 162, 0.2)

                        pyautogui.click(824, 162)
                        
                        time.sleep(7)
                        
                        
                        # Simula pressionamento de solicitar a impressão do pedido
                        pyautogui.moveTo(222, 89, 0.2)

                        pyautogui.click(222, 89)

                        time.sleep(0.3)
                        
                        pyautogui.hotkey('enter')

                        # time.sleep(0.3)
                        # pyautogui.hotkey('enter')

                        time.sleep(0.5)
                        
                        # planilha = planilha.drop(index)
                        # planilha.to_csv('pedidos.csv', index=False)
                        pyautogui.moveTo(677, 692)

                        pyautogui.click(677, 692)

                        time.sleep(0.2)

                        # # Simula pressionamento da atalho para fechar a aba aberta
                        pyautogui.hotkey('ctrl', 's')

                        time.sleep(2.5)
                        # Remove essa linha se deseja percorrer todos os IDs

                        # # Simula pressionamento do comando de atalho para iniciar um novo formulario de solicitação de pedido
                        pyautogui.hotkey('ctrl', 'i')
                        
                        time.sleep(0.5)
         
        print(f'Quantidade de pedidos empressos foram({numero_de_linhas}), Fim dos pedidos')        
                