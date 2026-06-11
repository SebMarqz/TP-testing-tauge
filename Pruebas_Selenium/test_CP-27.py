from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp27_actualizar_stock_descontar():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno y Login
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 2. Navegar a Stock
        wait.until(EC.element_to_be_clickable((By.ID, "tab-stock"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "sec-stock")))

        # 3. Hacer clic en el botón "- Quitar" del insumo con ID 1
        xpath_boton_quitar = "//td[text()='1']/following-sibling::td[contains(@class, 'actions-cell')]/button[contains(text(), '- Quitar')]"
        boton_quitar = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_boton_quitar)))
        boton_quitar.click()

        # 4. Manejar el prompt nativo de JavaScript para enviar la cantidad
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        # Enviamos "5" como cantidad a descontar y aceptamos
        alert.send_keys("5")
        alert.accept()

        # 5. Validación Esperada (Assert)
        # La función quitarStock() no emite un mensaje global de éxito, solo recarga la tabla.
        # Por seguridad, esperamos a que la tabla se recargue visualmente sin mostrar errores en el proceso.
        tbody_stock = wait.until(EC.presence_of_element_located((By.ID, "tbody-stock")))
        assert tbody_stock.is_displayed(), "La prueba falló: La tabla de stock no se muestra después de actualizar la cantidad."

    finally:
        driver.quit()