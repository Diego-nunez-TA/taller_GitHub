### Librerías
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from fake_useragent import UserAgent

### Raúl
def nbachamps_to_csv():
    print("Conectando a web...")
    datanba = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA', index_col=0)

    ### read_html devuelve una **lista de dataframes***. Esto de aquí abajo busca dónnde está el nombre de  
    ### una de las columnas,y devuelve aquella donde lo encuentra
    lookup_str = "Años campeón"
    nba_champs = next ((table for table in datanba if lookup_str in table.stack().to_string()))

    ###Terminamos printeando el df en el csv final
    print("Creando csv...")
    nba_champs.to_csv("rgg_nba_champs.csv")
    print("¡Terminado!")
    juegos_df = pd.DataFrame(dict_juegos)
    juegos_df.to_csv("best10games.csv")

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

    