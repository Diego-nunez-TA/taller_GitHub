# Dataframe con los anillos de la NBA que tiene cada equipo, con nombre, número de campeonatos y años campeón.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random

def waitAndClickElement(driver, elemento):
    """
    Espera a que un elemento sea clicable y hace clic en él.

    :param driver: WebDriver de Selenium.
    :param elemento: Valor del selector XPATH del elemento.
    """
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elemento))
        )
        # Hacer clic en el botón
        button.click()
        print(f"Hiciste clic en el botón {elemento}")
    except TimeoutException:
        print(f"El botón {elemento} no apareció o no es clicable")

def waitAndGetElement(driver, xpath, timeout=2):
    """
    Espera a que un elemento esté presente en la página y devuelve su texto.

    :param driver: WebDriver de Selenium.
    :param value: Valor del selector.
    :param timeout: Tiempo máximo de espera en segundos.
    :return: Texto del elemento o None si no se encuentra.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text
    except Exception as e:
        # print(f"Error: {e}")
        return None

# Lanzar el crhomedriver y preparar el driver
service = Service(executable_path='./chromedriver_alumno/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options) # Driver normal
# driver = webdriver.Chrome(service=service, options=chrome_options)

# Entramos en la pagina competiciones
driver.get("https://spain.id.nba.com/noticias/campeones-nba")

# Encuentrar el elemento  para hacer scroll
elemento = driver.find_element(By.XPATH, "//strong[text()='Esta es la clasificación completa por equipos:']")

# Moverse hasta el elemento
driver.execute_script("arguments[0].scrollIntoView();", elemento)


dict_anillos = {"nombre_equipo" : [],
                "n_titulos_ganados" : [],
                "años_titulos": []}

filas = driver.find_elements(By.XPATH,"(//strong[text()='Esta es la clasificación completa por equipos:']/../following-sibling::ol)[1]/li")
for fila in filas: 
    separado = fila.text.split(": ",1)
    nombre_equipo = separado[0]
    dict_anillos["nombre_equipo"].append(nombre_equipo)
    # print("nombre->",nombre_equipo)


    separado = separado[1].split(" (",1)
    n_titulos = separado[0]
    dict_anillos["n_titulos_ganados"].append(n_titulos)
    # print("n_titulos->",n_titulos)

    anios = separado[1].replace(")","")
    dict_anillos["años_titulos"].append(anios)
    # print("anios->",anios)

df = pd.DataFrame(dict_anillos)
print(df.head())

































"""




# obtener n  de filas y columnas
n_columnas = len(driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr[1]/th"))
n_filas = len(driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr"))

print("Nº filas",n_filas)
print("Nº columnas:",n_columnas)

# Obtener columnas
columnas_sel = driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr[1]/th")

columnas = []

for i,columna in enumerate(columnas_sel):
    columnas.append(columna.text)

print(columnas)

nombre_equipo = []
n_titulos_ganados = []
años_titulos = []

dict_anillos = {"nombre_equipo" : [],
                "n_titulos_ganados" : [],
                "años_titulos": []}
# dict_anillos = {"nombre_equipo" : [],
#                 "años_titulos": []}

dict_anillos = {"nombre_equipo" : [],
                "años_titulos": []
                }

for indice_columnas in range(n_columnas): # j = indice fila
    for indice_filas in range(n_filas):
        elemento_a_buscar = driver.find_elements(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]")
        if len(elemento_a_buscar)>0: # si existe, extraelo
            elemento = driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]").text
            # print(driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]").text)
            print(f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]-->",elemento)
            if indice_columnas == 0:
                dict_anillos["nombre_equipo"].append(elemento)



for indice_columnas in range(n_columnas): # j = indice fila
    for indice_filas in range(n_filas):
        elemento_a_buscar = driver.find_elements(By.XPATH, f"((//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td)//a[contains(@title,'NBA Finals')]")
        if len(elemento_a_buscar)>0: # si existe, extraelo
            for i in elemento_a_buscar:
            elemento = driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]").text
            # print(driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]").text)
            print(f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]-->",elemento)
            if indice_columnas == 0:
                dict_anillos["nombre_equipo"].append(elemento)


               
        #     elif indice_columnas == 1:
        #         try:
        #             dict_anillos["nombre_equipo"].append(elemento)
        #         except:
        #             dict_anillos["n_titulos_ganados"].append("NO")
        #     elif indice_columnas == 2:
        #         try:
        #             dict_anillos["nombre_equipo"].append(elemento)
        #         except:
        #             dict_anillos["años_titulos"].append("NO")
        # elif len(driver.find_elements(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]"))

        # try:
            
        # except:
        #     if indice_columnas == 0:
        #         dict_anillos["nombre_equipo"]= "NO"
        #     # elif indice_columnas == 1:
        #     #     dict_anillos["n_titulos_ganados"]= "NO"
        #     # elif indice_columnas == 2:
        #     #     dict_anillos["años_titulos"]= "NO"
        #     print(f"No se pudo sacar (//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{indice_filas+1}]//td[{indice_columnas+1}]")
                
        
        # # print(f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{j+1}]//td[{i+1}]")
        # if i != 0:
        #     print(driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{j+1}]//td[{i+1}]").text)
        # # print("j:",j)
        # # print("element:",element.text)


df = pd.DataFrame(dict_anillos)
print(df.head())




















#//table[@class="wikitable"]//tr[contains(.,"Años campeón")]

#driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr")








    


# for i in range(len(driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr[1]/th"))):
#     # if i == 0:
#     #     continue
#     try:
#         for j, element in enumerate(driver.find_elements(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{i+1}]//td")):
#             print(driver.find_element(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{i+1}]//td[{j+1}]").text)
#             # print("j:",j)
#             # print("element:",element.text)
#     except:
#         print("ese no")
          

     
     
    
# (//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[6]//td[3]

# for i, row in enumerate(driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr")):
#         for j in enumerate(driver.find_elements(By.XPATH, f"(//h2[@id='Número_de_campeonatos_por_equipo']/../following-sibling::table//tr)[{i}]//td")):
             
#         # if i == 0:
#         #     print("*"*50)
#         #     print("Es cero")
#         #     print(columna.text)
#         # elif i ==1:
#         #     print("*"*50)
#         #     print("Es UNO")
        #     print(columna.text)
        # elif i == 2:
        #     print("*"*50)
        #     print("Es DOS")
        #     print(columna.text)


# rows = driver.find_elements(By.XPATH, "//h2[@id='Número_de_campeonatos_por_equipo']")





# input("Presiona intro")

# # Al final, cerrar el navegador
# driver.quit()



"""


