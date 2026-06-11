from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp18_registrar_cliente_valido():
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

        # 3. Llenar formulario completo según datos del CP-18
        # Completamos el ID según especifica el caso de prueba
        driver.find_element(By.ID, "c-id").clear()
        driver.find_element(By.ID, "c-id").send_keys("1")
        
        driver.find_element(By.ID, "c-nombre").clear()
        driver.find_element(By.ID, "c-nombre").send_keys("Juan Perez")
        
        driver.find_element(By.ID, "c-telefono").clear()
        driver.find_element(By.ID, "c-telefono").send_keys("1122334455")
        
        driver.find_element(By.ID, "c-email").clear()
        driver.find_element(By.ID, "c-email").send_keys("juan@test.com")

        # 4. Enviar formulario
        # Ajustado al texto exacto que tiene tu botón en el HTML
        driver.find_element(By.XPATH, "//button[text()='Guardar Cliente']").click()

        # 5. Validación Esperada (Assert)
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        # Esperamos a que el mensaje de éxito sea visible
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))
        
        assert "success" in mensaje.get_attribute("class"), "La prueba falló: No se registró el cliente correctamente."

    finally:
        driver.quit()