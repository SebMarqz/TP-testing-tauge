import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from pathlib import Path

def test_cp07_modificar_pedido_entregado():
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

        # 2. Navegar a Pedidos
        wait.until(EC.element_to_be_clickable((By.ID, "tab-pedidos"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "sec-pedidos")))

        # 3. Buscar el botón Edit del pedido 1 (Protegido contra redibujado asíncrono)
        xpath_btn_editar = "//td[text()='1']/parent::tr//button[contains(., 'Edit')]"
        
        for intento in range(3):
            try:
                boton_editar = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_btn_editar)))
                boton_editar.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.5)
                continue

        # 4. Llenar el formulario con el intento de modificación
        wait.until(EC.visibility_of_element_located((By.ID, "p-desc")))
        driver.find_element(By.ID, "p-desc").clear()
        driver.find_element(By.ID, "p-desc").send_keys("Intento modificar pedido entregado")

        # 5. Intentar guardar los cambios
        driver.find_element(By.XPATH, "//button[text()='Guardar Pedido']").click()

        # 6. Validación Esperada (Assert)
        # Esperamos que el backend rechace la operación y se muestre la clase "error"
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "error" in mensaje.get_attribute("class") or "hidden" not in mensaje.get_attribute("class"))
        
        assert "error" in mensaje.get_attribute("class"), "La prueba falló: El sistema no bloqueó la modificación del pedido entregado."

    finally:
        driver.quit()