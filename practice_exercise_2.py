import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

driver.implicitly_wait(5)
# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("burgos.137@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.XPATH, "//button[@class='auth-form__button']").click()


# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))


# Guardar el título de la tarjeta más reciente
items_list = driver.find_elements(By.XPATH, "//ul[@class='places__list']/li")
title_before = items_list[0].find_element(By.CLASS_NAME, "card__title").text

# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(By.CLASS_NAME,"profile__add-button").click()

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
randomInt = random.randint(100,999)
new_title = "tokyo"+ str(randomInt)
new_link = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg"
driver.find_element(By.XPATH, "//form[@name='new-card']//input[@id='place-name']").send_keys(new_title)

# Insertar el enlace a la imagen en el campo Enlace
driver.find_element(By.XPATH, "//form[@name='new-card']//input[@id='place-link']").send_keys(new_link)

# Guardar los datos
driver.find_element(By.XPATH, "//form[@name='new-card']/button[text()='Guardar']").click()

# Esperar a que aparezca el botón Eliminar
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
    By.XPATH,"//li[1]//button[@class='card__delete-button card__delete-button_visible']")))
time.sleep(3)
# Comprobar que la tarjeta tiene el título correcto
title_after = driver.find_element(By.XPATH, "//li[1]//div[@class='card__description']//h2[@class='card__title']").text
assert title_after == new_title

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(driver.find_elements(By.XPATH, "//ul[@class='places__list']/li"))

# Eliminar la tarjeta
driver.find_element(By.XPATH, "//li[1]//button[@class='card__delete-button card__delete-button_visible']").click()
time.sleep(3)
# Esperar a que el título de la tarjeta más reciente sea igual a title_before
WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"//li[1]//div[@class='card__description']//h2[@class='card__title']"),title_before))

# Comprobar que ahora hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, "//ul[@class='places__list']/li"))
# print("cards after ", cards_after)
# print("cards before ", cards_before)
assert cards_after < cards_before

driver.quit()
