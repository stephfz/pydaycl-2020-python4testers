'''
Script de prueba que verificar que la lista "Modelo" contenga elementos
Para ver el bug(si aun sigue en la web) descomentar Daewoo y comentar Alfa Romeo
'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.segurosimple.com/")

element = driver.find_element_by_id("Marca")
#modelo = "Daewoo"
modelo = "Alfa-Romeo"
element.send_keys(modelo)

annio_fabricacion = "2008"
element = driver.find_element_by_id("Año")
element.send_keys(annio_fabricacion)


element = driver.find_element_by_id("Modelo")
assert len(element.text) > len(":: Seleccione ::"), \
        "Los modelos de la marca %s no fueron cargados" % modelo
modelo = "147 1.6 TI"
element.send_keys(modelo)

driver.find_element_by_id("TelefonoCotizacion").send_keys("997261789")

element = driver.find_element_by_id("EmailCotizacion")
element.send_keys("mimail@yahoo.com")

element = driver.find_element_by_id("edadUsuario")
element.send_keys("30")


driver.find_element_by_id("btnComparar").click()

# Mala practica fines visuales
time.sleep(3)
driver.quit()
