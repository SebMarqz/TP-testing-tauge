from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp21_visualizar_cliente():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación y Login
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 2. Navegar a Clientes
        wait.until(EC.element_to_be_clickable((By.ID, "tab-clientes"))).click()
        
        # 3. Validación Esperada (Assert)
        # Verificamos que la sección principal de clientes esté visible
        sec_clientes = wait.until(EC.presence_of_element_located((By.ID, "sec-clientes")))
        wait.until(lambda d: "hidden" not in sec_clientes.get_attribute("class"))
        
        assert sec_clientes.is_displayed(), "La prueba falló: No se pudo visualizar el panel de clientes."

    finally:
        driver.quit()