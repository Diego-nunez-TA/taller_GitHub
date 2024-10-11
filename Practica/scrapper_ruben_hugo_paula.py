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