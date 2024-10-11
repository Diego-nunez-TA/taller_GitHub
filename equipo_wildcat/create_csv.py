### Raúl - ¿qué opináis de aunar sección de librerías??
import pandas as pd

# Manuel

# Sengan

# Alejandro

# Raúl
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


### Raúl - Si vamos todos a funciones, ¿qué opináis de ejecutarlas todas aquí abajo?
nbachamps_to_csv()