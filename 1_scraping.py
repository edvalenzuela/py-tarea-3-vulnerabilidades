from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
URL_BASE = 'https://backtrackacademy.com/users/sign_in'
#driver.get("https://edvalenzuela.github.io/")
driver.get(URL_BASE)
#driver.maximize_window()
time.sleep(2) 

usuario = driver.find_element("id", 'user_email')
clave = driver.find_element('id', 'user_password')

usuario.send_keys("edvalenzuelap@gmail.com")
clave.send_keys("yoamolausach")

time.sleep(2) 

boton = driver.find_element('name', 'commit')
boton.click()

time.sleep(2) 

matches = driver.find_elements(By.CLASS_NAME, "glitch")

def getNamesOfCourses():
  cont = 0
  if isinstance(matches, list) and type(matches) == list:
    print("=== Listado de cursos de backtrackacademy ===\n")
    for i in matches:
        cont+=1
        print("{} - {}".format(cont, i.text))
  else : print("\n === No hay datos para mostrar ===".upper())

getNamesOfCourses()
driver.close()
