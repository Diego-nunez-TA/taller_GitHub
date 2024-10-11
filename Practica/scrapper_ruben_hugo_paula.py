pd.set_option('max_colwidth', 800)

url2 = "https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA"
response2 = requests.get(url2)

print(response2)

html2 = response2.content

soup2 = bs(html2, 'html.parser')

df3: {"Equipo" : [],
      "Campeonato" : [],
      "Años Campeón" : []}


for x in soup2.find_all('tr'):
    print(x.get_text())

table = soup2.find('table', {"class": "wikitable"})

# Iterar por cada fila de la tabla, excluyendo el encabezado
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    
    # Asegúrate de que la fila tenga suficientes columnas
    if len(cells) >= 3:
        equipo = cells[0].get_text(strip=True)
        campeonatos = cells[1].get_text(strip=True)
        anios = cells[2].get_text(strip=True)
        
        df3["Equipo"].append(equipo)
        df3["Campeonato"].append(campeonatos)
        df3["Años Campeón"].append(anios)

# Si quieres crear un DataFrame a partir del diccionario
df_final = pd.DataFrame(df3)
print(df_final)
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

url_1 = "https://es.wikipedia.org/wiki/Ochomil"
response_1 = requests.get(url_1)


soup_1 = bs(response_1.content, 'html.parser')

table_1 = soup_1.find_all('table')[1]


nombres_1 = []
for row in table_1.find_all('tr'):
    celdas = row.find_all('td')
    if len(celdas) > 1:
        link = celdas[1].find('a')
        nombres_1.append(link.get_text())
 



alturas_1 = []
for row in table_1.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) > 2:
        texto = cells[2].get_text(strip=True)
        altura = re.findall(r'\d+', texto)
        if altura:
            alturas_1.append(altura[0])

tamaño_1 = alturas_1[-14:]


paises_1 = []
for row in table_1.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) > 3:
        enlace = cells[3].find('a')
        if enlace:
            pais = enlace.get_text(strip=True)
            paises_1.append(pais)


montañas_1 = {"Nombre": nombres_1,
            "Altura": alturas_1,
            "País": paises_1}

df_montañas = pd.DataFrame(montañas_1)
df_montañas