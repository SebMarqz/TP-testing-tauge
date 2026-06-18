from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp19_registrar_cliente_sin_nombre():
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
        wait.until(EC.presence_of_element_located((By.ID, "sec-clientes")))

        # 3. Llenar formulario dejando el nombre vacío
        driver.find_element(By.ID, "c-nombre").clear()
        
        driver.find_element(By.ID, "c-telefono").clear()
        driver.find_element(By.ID, "c-telefono").send_keys("1122334455")
        
        driver.find_element(By.ID, "c-email").clear()
        driver.find_element(By.ID, "c-email").send_keys("cliente@test.com")

        # 4. Enviar formulario
        driver.find_element(By.XPATH, "//div[@id='sec-clientes']//button[contains(text(), 'Registrar') or contains(text(), 'Guardar')]").click()

        # 5. Validación Esperada (Assert)
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "error" in mensaje.get_attribute("class") or "hidden" not in mensaje.get_attribute("class"))
        
        assert "error" in mensaje.get_attribute("class"), "La prueba falló: El sistema no validó la falta de nombre."

    finally:
        driver.quit()