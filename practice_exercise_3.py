import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
driver.implicitly_wait(5)

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("burgos.137@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.XPATH, "//button[@class='auth-form__button']").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

time.sleep(2)

# Buscar la tarjeta y desplazarla a la vista
element = driver.find_element(By.XPATH, "//li[1]")
driver.execute_script("arguments[0].scrollIntoView();",element)

time.sleep(2)


driver.quit()
