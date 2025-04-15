from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

# Configurações do dispositivo
desired_caps = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "Pixel_6_Pro",
    "app": "/caminho/para/app-debug.apk",
    "automationName": "UiAutomator2"
}

@pytest.fixture
def driver():
    # Inicializa a sessão no Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

def test_login_success(driver):
    # Localiza elementos e interage com o app
    campo_email = driver.find_element(AppiumBy.ID, "com.app.example:id/email")
    campo_senha = driver.find_element(AppiumBy.ID, "com.app.example:id/password")
    botao_login = driver.find_element(AppiumBy.ID, "com.app.example:id/login_btn")

    campo_email.send_keys("usuario@teste.com")
    campo_senha.send_keys("senha123")
    botao_login.click()

    # Verifica se o login foi bem-sucedido
    mensagem = driver.find_element(AppiumBy.ID, "com.app.example:id/welcome_text")
    assert "Bem-vindo" in mensagem.text

def test_login_fail(driver):
    # Teste com credenciais inválidas
    campo_email = driver.find_element(AppiumBy.ID, "com.app.example:id/email")
    campo_senha = driver.find_element(AppiumBy.ID, "com.app.example:id/password")
    botao_login = driver.find_element(AppiumBy.ID, "com.app.example:id/login_btn")

    campo_email.send_keys("email_invalido@teste.com")
    campo_senha.send_keys("senha_errada")
    botao_login.click()

    mensagem_erro = driver.find_element(AppiumBy.ID, "com.app.example:id/error_text")
    assert "Credenciais inválidas" in mensagem_erro.text