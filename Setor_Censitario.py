import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Passo 1: Carregar a planilha Excel com pandas
df = pd.read_excel('C:/Users/acpereira/OneDrive - Echostar Operating L.L.C/Documents/Atividades pontuais/Serviços por Área/Apoio/Preencher_UF.xlsx')

# Supondo que as colunas da planilha sejam 'Latitude' e 'Longitude'
# Passo 2: Criar uma GeoDataFrame com as coordenadas
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
pontos = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")  # EPSG:4326 é o sistema de coordenadas padrão (WGS 84)

# Passo 3: Carregar o shapefile dos setores censitários do IBGE
setores = gpd.read_file('G:/MARKETING & COMUNICAÇÃO/PLANEJAMNETO COMERCIAL/Relatórios Power BI/Field_Services/BR_Malha_Preliminar_2022/BR_Malha_Preliminar_2022.shp')

# Passo 4: Realizar o join espacial para obter o setor censitário correspondente
setores_censitarios = gpd.sjoin(pontos, setores, how="left", predicate="within")

# Passo 5: Exportar os resultados para um novo arquivo Excel (opcional)
setores_censitarios.to_excel('C:/Users/acpereira/OneDrive - Echostar Operating L.L.C/Documents/Atividades pontuais/Serviços por Área/Apoio/Preencher_UF.xlsx', index=False)


print("Processo concluído. Resultados salvos em 'resultado_setores.xlsx'")


