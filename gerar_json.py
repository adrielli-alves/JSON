import geopandas as gpd
from shapely.geometry import Point
import json
 
# Lista de coordenadas das cidades
coordenadas = []


# Cria um GeoDataFrame a partir das coordenadas das cidades
pontos = [Point(lon, lat) for lon, lat in coordenadas]
gdf = gpd.GeoDataFrame(geometry=pontos)

# Calcula a envoltória convexa (convex hull)
envoltoria_convexa = gdf.geometry.unary_union.convex_hull
print(list(envoltoria_convexa.exterior.coords))

# Cria o dicionário no formato GeoJSON
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "MR ABELARDO LUZ",
                "description": "MR ABELARDO LUZ"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [list(envoltoria_convexa.exterior.coords)]
            }
        }
    ]
}

# Exibe o JSON resultante
#print(json.dumps(geojson, indent=2))

# Salva o resultado em um arquivo .json
with open('regiao_cidades.json', 'w') as f:
    json.dump(geojson, f, indent=2)
