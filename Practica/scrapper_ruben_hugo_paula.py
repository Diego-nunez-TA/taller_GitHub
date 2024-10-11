from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re

url_1 = "https://es.wikipedia.org/wiki/Ochomil"
response_1 = requests.get(url_1)

soup_1 = bs(response_1.content, 'html.parser')

table_1 = soup_1.find_all('table')[1]


def extraer_nombres(table):
    nombres = []
    for row in table.find_all('tr'):
        celdas = row.find_all('td')
        if len(celdas) > 1:
            link = celdas[1].find('a')
            if link:
                nombres.append(link.get_text())
    return nombres


def extraer_alturas(table):
    alturas = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 2:
            texto = cells[2].get_text(strip=True)
            altura = re.findall(r'\d+', texto)
            if altura:
                alturas.append(altura[0])
    return alturas[-14:]


def extraer_paises(table):
    paises = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 3:
            enlace = cells[3].find('a')
            if enlace:
                paises.append(enlace.get_text(strip=True))
    return paises


def crear_dataframe(nombres, alturas, paises):
    montañas = {
        "Nombre": nombres,
        "Altura": alturas,
        "País": paises
    }
    return pd.DataFrame(montañas)