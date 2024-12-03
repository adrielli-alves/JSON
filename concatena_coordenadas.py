import json
import pandas as pd
import re
import geopandas as gpd
from shapely.geometry import Point
import ast

# Carregar o arquivo Excel
# Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo
df = pd.read_excel('teste_coordenadas.xlsx', header=None, names=["Cidade", "MicroRegiao", "Coordenadas"])

# Função para limpar e converter a string das coordenadas em uma lista
def parse_coordinates(coord_str):
    # Remover espaços extras
    coord_str = coord_str.strip()
    
    # Imprimir as coordenadas para depuração
    #print(f"Verificando coordenadas: {coord_str}")
    
    # Usar uma expressão regular para limpar coordenadas mal formadas, como aspas extras ou outros caracteres
    coord_str = re.sub(r'["\']', '', coord_str)  # Remover aspas extras se houver
    
    # Garantir que a string comece com '[' e termine com ']'
    if coord_str.startswith('[') and coord_str.endswith(']'):
        try:
            return ast.literal_eval(coord_str)
        except (ValueError, SyntaxError) as e:
            print(f"Erro ao converter coordenadas: {coord_str}. Erro: {e}")
            return []  # Caso haja erro, retornamos uma lista vazia
    else:
        print(f"Formato inválido para coordenadas: {coord_str}")
        return []

def remove_coordenadas_duplicadas(coordenadas):
    # Criar uma lista a partir das coordenadas removendo todas as duplicadas
    return 0


# Aplicando a função para criar a coluna de coordenadas como listas
df['Coordenadas'] = df['Coordenadas'].apply(parse_coordinates)

# Agrupando os dados pela micro região e concatenando as coordenadas
micro_regioes = df.groupby('MicroRegiao')['Coordenadas'].apply(lambda x: [coord for sublist in x for coord in sublist]).reset_index()

for i in range(len(micro_regioes)):
    coordenadas_finais = remove_coordenadas_duplicadas(micro_regioes.loc[i, 'Coordenadas'])
    micro_regioes.loc[i, 'Coordenadas'] = coordenadas_finais

    #print(coordenadas_finais)

# Criar um novo DataFrame para a nova aba
result_df = micro_regioes[['MicroRegiao', 'Coordenadas']]

# Salvar no Excel, criando uma nova aba chamada "MicroRegioes_Concatenadas"
with pd.ExcelWriter('teste_coordenadas_atualizado.xlsx', engine='xlsxwriter') as writer:
    # Salvar a aba original
    df.to_excel(writer, sheet_name='Original', index=False)
    
    # Salvar a nova aba com as micro regiões e coordenadas
    result_df.to_excel(writer, sheet_name='MicroRegioes_Concatenadas', index=False)

print("Novo arquivo com a aba 'teste_coordenadas' foi salvo com sucesso!")