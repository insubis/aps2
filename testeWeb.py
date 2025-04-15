from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# URL do site
driver.get("https://www.saucedemo.com")

# ---------- LOGIN ----------
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(2)

# ---------- VALIDAÇÃO DE UI ----------
assert "Swag Labs" in driver.title
print("[OK] T Título validado com sucesso!")
time.sleep(2)
# Verifica visibilidade de um elemento importante
inventory_container = driver.find_element(By.ID, "inventory_container")
assert inventory_container.is_displayed()
print("[OK] Título validado com sucesso!")
time.sleep(2)

# ---------- TESTE DE CRUD NO CARRINHO ----------
add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_button.click()
print("[OK] T Item adicionado ao carrinho!")
time.sleep(2)

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
time.sleep(2)


cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
assert cart_item.is_displayed()
print("[OK] T Item presente no carrinho!")
time.sleep(2)

remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
remove_button.click()
time.sleep(1)
print(" Item removido do carrinho!")

try:
    driver.find_element(By.CLASS_NAME, "cart_item")
    print(" Item ainda no carrinho!")
except:
    print("Carrinho vazio!")
    
time.sleep(2)
driver.quit()
