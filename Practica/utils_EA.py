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
service = Service(executable_path='./chromedriver_alumno/chromedriver_Fran.exe')
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


# ------------------------------------------------------------------------
# ----------------- PARTE ANA -------------------------
# ------------------------------------------------------------------------

url = "https://es.m.wikipedia.org/wiki/Anexo:Libros_m%C3%A1s_vendidos"
selenium_path = "../../../Selenium_eject/chromedriver.exe"
# ejecutar seleniumm y extraer datos
def libros_mas_vendidos(url):
    service = Service(executable_path= selenium_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    tabla = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[3]/div/div[1]/section[2]/table')
    filas = tabla.find_elements(By.TAG_NAME, "tr")
    columnas = []
    datos = []
    for fila in filas:
        etiquetas = fila.find_elements(By.TAG_NAME,"th")
        for etiqueta in etiquetas:
            columnas.append(etiqueta.text)
        valores = fila.find_elements(By.TAG_NAME,"td")
        for valor in valores:
            datos.append(valor.text)
    datos_arr = np.array(datos)
    datos_arr = datos_arr.reshape((10,5))
    libros_mas_vendidos = pd.DataFrame(datos_arr, columns=columnas)
    libros_mas_vendidos.to_csv("libros_mas_vendidos.csv")

libros_mas_vendidos(url)





