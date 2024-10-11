MAIN


# PAULA

url = "https://es.wikipedia.org/wiki/Anexo:Libros_m%C3%A1s_vendidos" 

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
import requests
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)
print(response)