from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(2)

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("burgos.137@gmail.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("12345")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.XPATH, "//button[@class='auth-form__button']").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
time.sleep(2)
# Buscar el pie de página
element = driver.find_element(By.CLASS_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)

# Comprobar que el pie de página contiene el string 'Around'
assert element.text in "around"

driver.quit()
