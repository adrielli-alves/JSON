import ast
import pandas

# Caminho do arquivo
caminho_arquivo = 'geojs completo.txt'
excel = pandas.read_excel('coordenadas.xlsx', None)
excel = excel['Sheet1']


# Lista para armazenar as cidades e as coordenadas
cidades = []
coordenadas = []
teste = []

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

    # Identificar as cidades
    cidade = linha[linha.find('"name'):linha.find('", "description')]
    cidade = cidade.removeprefix('"name": "')
    cidades.append(cidade)

    # Identificar as coordenadas
    coordenada = linha[linha.find('"coordinates": [['):linha.find(']] }}')]
    coordenada = coordenada.removeprefix('"coordinates": [[')

    coordenada = ast.literal_eval(f"[{coordenada}]")
    teste.append(coordenada)

for i in range(len(cidades)):
    linhas = excel['coordenadas'].count()

    cidade = cidades[i].replace(' ', '_')
    cidade = cidade.replace("'", '_')

    armazenar = str(cidade) + " = " + str(teste[i])
    excel.loc[linhas, 'coordenadas'] = armazenar

excel.to_excel('coordenadas.xlsx', index=False)