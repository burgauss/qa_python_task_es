import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(3)

# Buscar elementos
email = driver.find_element(By.CSS_SELECTOR, "#email")
password = driver.find_element(By.CSS_SELECTOR, "#password")

# Probar el atributo placeholder para cada elemento
assert email.get_attribute('placeholder') == "Correo electrónico"
assert password.get_attribute('placeholder') == "Contraseña"

# Cerrar el navegador
driver.quit()
