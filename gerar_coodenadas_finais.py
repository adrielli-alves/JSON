import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import ast

def calcular_envoltoria_convexa(coordenadas):
    """
    Recebe uma lista de coordenadas e calcula a envoltória convexa (convex hull) para elas,
    retornando as coordenadas finais da envoltória.
    """
    # Criar uma lista de objetos Point a partir das coordenadas
    pontos = [Point(lon, lat) for lon, lat in coordenadas]
    # Criar um GeoDataFrame a partir dos pontos
    gdf = gpd.GeoDataFrame(geometry=pontos)
    
    # Usar union_all() para combinar as geometrias e calcular a envoltória convexa
    envoltoria_convexa = gdf.geometry.union_all().convex_hull
    
    # Retorna as coordenadas da envoltória convexa
    return list(envoltoria_convexa.exterior.coords)

def processar_arquivo_excel(input_file, output_file):
    """
    Processa um arquivo Excel, aplicando a transformação de coordenadas para cada micro região
    e salvando os resultados em um novo arquivo Excel.
    """
    # Ler o arquivo Excel
    df = pd.read_excel(input_file)
    
    # Criar lista para armazenar as coordenadas finais
    coordenadas_finais = []
    
    # Iterar por cada linha do DataFrame
    for index, row in df.iterrows():
        # Recuperar a coordenada inicial da linha (em formato de lista)
        coordenada_inicial = ast.literal_eval(row['Coordenada inicial'])
        
        # Calcular a envoltória convexa das coordenadas iniciais
        coordenada_final = calcular_envoltoria_convexa(coordenada_inicial)
        
        # Adicionar a coordenada final à lista
        coordenadas_finais.append(coordenada_final)
    
    # Adicionar a nova coluna de coordenadas finais ao DataFrame
    df['Coordenada final'] = coordenadas_finais
    
    # Salvar o DataFrame com as novas coordenadas em um arquivo Excel
    df.to_excel(output_file, index=False)

    print(f"Processamento concluído. Arquivo de saída salvo como '{output_file}'.")

# Caminhos para os arquivos de entrada e saída
input_file = 'entrada.xlsx'  # Caminho para o arquivo Excel de entrada
output_file = 'saida.xlsx'   # Caminho para o arquivo Excel de saída

# Processar o arquivo
processar_arquivo_excel(input_file, output_file)
