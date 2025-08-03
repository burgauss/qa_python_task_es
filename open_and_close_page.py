from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la página del banco de pruebas
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')

# Comprobar que /signin se agrega a la URL
time.sleep(2)
if '/signin' in driver.current_url:
    print("Redirected to signin page.")
else:
    print("Not on signin page.")

# Cerrar el navegador
driver.quit()
