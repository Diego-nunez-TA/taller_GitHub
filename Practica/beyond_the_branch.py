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

#función scrape: Top10Libros
def top_books_scrape():
    url = 'https://en.wikipedia.org/wiki/List_of_best-selling_books'
    response1 = pd.read_html(url, header=0)[0]
    response2 = pd.read_html(url, header=0)[1]
    top_10_books = pd.concat([response1.iloc[:,[0,1,3]], response2.iloc[0:2, [0,1,3]]], ignore_index=True)
    top_10_books.to_csv('top_10_wiki_books.csv')