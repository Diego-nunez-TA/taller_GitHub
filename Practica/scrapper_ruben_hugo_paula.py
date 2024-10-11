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