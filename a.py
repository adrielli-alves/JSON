# Caminho do arquivo
caminho_arquivo = 'geojs.txt'
IDs = []
cidades = []
coordenadas = []

# Tentando abrir o arquivo com uma codificação específica
try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.readlines()  # Lê todas as linhas
except UnicodeDecodeError:
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        texto = arquivo.readlines()  # Lê todas as linhas

# Total de linhas para percorrer
total_linhas = len(texto)

# Para cada linha percorrida, identificar o nome e as coordenadas
for i in range(total_linhas-2):
    linha = texto[i+1]

    #ID
    id = linha[linha.find('{"id'):linha.find('", "name"')]
    id = id.removeprefix('{"id": "')
    IDs.append(id)

    # Identificar as cidades
    cidade = linha[linha.find('"name'):linha.find('", "description')]
    cidade = cidade.removeprefix('"name": "')
    cidades.append(cidade)

    # Identificar as coordenadas
    coordenada = linha[linha.find('"coordinates": [['):linha.find(']]] }}')]
    coordenada = coordenada.removeprefix('"coordinates": [[')
    lista = coordenada.split(", ")
    item_lista = ""
    coord_lista = []
    coord_lista_apoio = []

    for i in range(len(lista)):
        coord = lista[i].removesuffix(']')
        coord = coord.removeprefix('[')
        coord_int = list(map(float, coord.split(',')))
        coord_lista_apoio.append(coord_int)

        if i%2 != 0 and i != 0:
            coord_lista.append(coord_lista_apoio)
            coord_lista_apoio = []

    coordenadas.append(coord_lista)

    for i in range(len(coordenadas)):
        print(coordenadas[i], "\n")
    

'''# Definição de linhas padrões
primeira_linha = '{ "type": "FeatureCollection", "features": ['
ultima_linha = '\n] }'
inicio = '{ "type": "Feature", "properties": {"id": "'

# Imprimir IDs, cidades e as coordenadas
for i in range(len(cidades)):
    if i == 0:
        print(primeira_linha + "\n" + inicio + IDs[i] + '", "name": "' + cidades[i] + '", "description": "' + cidades[i] + '"}, "geometry": { "type": "Polygon", "coordinates": [' + str(coordenadas[i]) + '] }},')
    elif i == len(cidades) - 1:
        print(inicio + IDs[i] + '", "name": "' + cidades[i] + '", "description": "' + cidades[i] + '"}, "geometry": { "type": "Polygon", "coordinates": [' + str(coordenadas[i]) + '] }}' + ultima_linha)
    else:
        print(inicio + IDs[i] + '", "name": "' + cidades[i] + '", "description": "' + cidades[i] + '"}, "geometry": { "type": "Polygon", "coordinates": [' + str(coordenadas[i]) + '] }},')

# Fim do programa'''