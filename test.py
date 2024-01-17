import pandas as pd

# Supondo que 'dados' seja o seu DataFrame
dados = pd.read_excel('pedidos.xlsx')

# Verificar o número de linhas no DataFrame
numero_de_linhas = len(dados)

if numero_de_linhas != 0:
    print(f"O DataFrame contém {numero_de_linhas} linha(s) de dados.")
else:
    print( 'O data frame está vazio')