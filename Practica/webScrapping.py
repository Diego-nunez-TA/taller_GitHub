from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Especifica la ruta correcta a chromedriver.exe
# Si chromedriver.exe está en el mismo directorio que este script, usa './chromedriver.exe'
service = Service(executable_path='./chromedriver.exe')

# Configuración de las opciones de Chrome
options = webdriver.ChromeOptions()
# No agregamos la opción de modo headless para permitir la interfaz gráfica

# Inicializa el controlador de Chrome
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abre la página web
    driver.get("http://www.google.es")

    # Espera 5 segundos para asegurarte de que la página se cargue completamente
    time.sleep(5)

    # Aquí puedes agregar el código para interactuar con la página o extraer información
    # Ejemplo: Busca el campo de búsqueda en Google y escribe una consulta
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Espera 5 segundos para que se carguen los resultados
    time.sleep(5)

    # Extrae los resultados de la búsqueda
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for result in results:
        print(result.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Asegúrate de que el navegador se cierre
    driver.quit()