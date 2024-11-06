import geopandas as gpd
from shapely.geometry import Point, MultiPoint
import json

# Lista de coordenadas das cidades (exemplo com 3 cidades)
coordenadas = [
    [-62.1820888570, -11.8668597878], [-62.1622953938, -11.8713991426], [-62.1570633807, -11.8704157362],  # Brasília
    [-62.5359497334, -9.7318235272], [-62.5078156831, -9.7542128151], [-62.5071949714, -9.7610327028], [-62.4931988248, -9.7722945792], [-62.4656434329, -9.7779520607], [-62.4554751520, -9.7735643212], [-62.4487884003, -9.7798371306], [-62.4352854171, -9.7801295280],  # Rio de Janeiro
    [-60.3993982597, -13.4558418276], [-60.4019491936, -13.4624655514], [-60.4110062797, -13.4612474089], [-60.4298714389, -13.4815495671], [-60.4314783557, -13.4880249017], [-60.4558394398, -13.4931111498], [-60.4650616449, -13.4887040376], [-60.4784798458, -13.4925849602], [-60.4812157546, -13.4964412072], [-60.4858953409, -13.4937695434], [-60.4950914439, -13.4993107533],          # Centro geográfico do Brasil
]

# Cria um GeoDataFrame a partir das coordenadas das cidades
pontos = [Point(lon, lat) for lon, lat in coordenadas]
gdf = gpd.GeoDataFrame(geometry=pontos)

# Calcula a envoltória convexa (convex hull)
envoltoria_convexa = gdf.geometry.unary_union.convex_hull

# Cria o dicionário no formato GeoJSON
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Micro Regiao 1",
                "description": "Micro Regiao 1"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [list(envoltoria_convexa.exterior.coords)]
            }
        }
    ]
}

# Exibe o JSON resultante
print(json.dumps(geojson, indent=2))

# Salva o resultado em um arquivo .json
with open('regiao_cidades.json', 'w') as f:
    json.dump(geojson, f, indent=2)
