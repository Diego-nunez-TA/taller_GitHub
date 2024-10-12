from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
import datetime

now = str(datetime.datetime.now())[5:19].replace('-', '_').replace(':', '_').replace(' ', '-')
url = 'https://es.wikipedia.org/wiki/Anexo:Libros_m%C3%A1s_vendidos'
response = requests.get(url)
html = response.content
soup = bs(html, 'html.parser')

libros_info = {'Titulo' : [x.find_all('td')[0].get_text() for x in soup.find_all('table')[0].find_all('tr')[1:] if x.find_all('td')],
            'Autor' : [x.find_all('td')[1].get_text() for x in soup.find_all('table')[0].find_all('tr')[1:] if x.find_all('td')],
            'Publicacion' : [x.find_all('td')[3].get_text() for x in soup.find_all('table')[0].find_all('tr')[1:] if x.find_all('td')]}

top_libros_df = pd.DataFrame(libros_info)

top_libros_df.to_csv('top_libros_'+now+'.csv')