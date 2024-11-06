def editar_coordenadas(coordenadas):
    total = "["
    for j in range(len(coordenadas)):
        dupla = coordenadas[j]

        for k in range(len(dupla) -1):

            if j == len(coordenadas) - 1:
                coor = "[" + str(dupla[k]) + ", " + str(dupla[k + 1]) + "]"
                total += str(coor)
            else:
                coor = "[" + str(dupla[k]) + ", " + str(dupla[k + 1]) + "], "
                total += str(coor)
        
    total += "]"
    return total



# Caminho do arquivo
caminho_arquivo = 'geojs.txt'
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
for i in range(total_linhas - 2):
    linha = texto[i + 1]

    # Identificar as coordenadas
    coordenada = linha[linha.find('"coordinates": [['):linha.find(']]] }}')]
    coordenada = coordenada.removeprefix('"coordinates": [[')
    lista = coordenada.split(", ")
    coord_lista = []
    coord_lista_apoio = []


    for i in range(len(lista)):
        coord = lista[i].removesuffix(']')
        coord = coord.removeprefix('[')
        coord_int = list(map(float, coord.split(',')))  # Converte as coordenadas para float
        coord_lista_apoio.append(coord_int)

        if i % 2 != 0 and i != 0:
            coord_lista.append(coord_lista_apoio)
            coord_lista_apoio = []

    coordenadas.append(coord_lista)

# Resultado final
for i in range(len(coordenadas)):
    coord = editar_coordenadas(coordenadas[i])

