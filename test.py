import pandas as pd

# Supondo que 'dados' seja o seu DataFrame
dados = pd.read_excel('pedidos.xlsx')

for index, row in dados.iterrows():
    id_selecionado = row['id']
    
    # Aqui você pode realizar as operações que deseja com o ID selecionado
    # Por exemplo, imprimir o ID selecionado
    print("ID selecionado:", id_selecionado)
    
    # Ou então, fazer alguma operação com o ID selecionado
    
    # Para sair do loop após o primeiro ID selecionado, remova o 'break' abaixo
    dados = dados.drop(index)
    dados.to_excel('pedidos.xlsx', index=False)
    # Verificar o número de linhas no DataFrame
    numero_de_linhas = len(dados)
    print(f"O DataFrame contém {numero_de_linhas} linha(s) de dados.")

# if numero_de_linhas != 0:
#     print(f"O DataFrame contém {numero_de_linhas} linha(s) de dados.")
# else:
#     print( 'O data frame está vazio')