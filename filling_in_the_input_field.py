from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
WebDriverWait(driver, 3).until(presence_of_element_located((By.ID, "email")))

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("burgos.137@gmail.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("12345")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.XPATH, "//button[@class='auth-form__button']").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(presence_of_element_located((By.XPATH, "//p[contains(text(), 'burgos.137')]")))

# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/signin?lng=es'
assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/signin?lng=es'

driver.quit()
