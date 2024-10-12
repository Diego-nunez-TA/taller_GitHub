#Importamos todos los paquetes que necesitamos
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from io import StringIO

#Dataframe con los anillos de la NBA que tiene cada equipo (nombre, número de campeonatos y años campeón)
url_wiki_nba = "https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA#Campeones_de_la_NBA"
page = requests.get(url_wiki_nba)
soup = BeautifulSoup(page.content, 'html.parser')
tbl = soup.find_all("table",{"class": "wikitable"})
nba_df = pd.read_html(StringIO(str(tbl[4])))[0]
nba_df.to_csv("nba_rings.csv")