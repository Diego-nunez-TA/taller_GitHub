from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from fake_useragent import UserAgent

ua = UserAgent()
#Dataframe con los 10 juegos más vendidos de la historia, con título, desarrollador y fecha de lanzamiento. Manuel
def create_games_csv():
    url = "https://vandal.elespanol.com/noticia/1350759936/los-juegos-mas-vendidos-de-la-historia-hasta-la-fecha-2023/"
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = bs(response.content, 'html.parser')

    dict_juegos ={
        "Titulo": [x.get_text().split(". ")[1].split(" -")[0] for x in soup.find_all("h3")[:10]],
        "Desarrollador": [x.get_text()[16:].split("Fecha")[0] for x in soup.find_all("ul")[6:16]],
        "Fecha de lanzamiento": [x.text.split("Fecha de lanzamiento: ")[1][0:4] for x in soup.find_all("li") if x.text.startswith("Fecha de lanzamiento:")]
        }

    juegos_df = pd.DataFrame(dict_juegos)
    juegos_df.to_csv("best10games.csv")