from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re # Expresiones regulares 
import time
import pandas as pd
import numpy as np

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