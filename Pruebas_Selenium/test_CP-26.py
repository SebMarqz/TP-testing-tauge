from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp26_alerta_stock_bajo():
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

        # 3. Ingresar los datos del Insumo bajo mínimo (Datos CP-26)
        driver.find_element(By.ID, "s-id").clear()
        driver.find_element(By.ID, "s-id").send_keys("1")
        
        driver.find_element(By.ID, "s-nombre").clear()
        driver.find_element(By.ID, "s-nombre").send_keys("Vinilo")
        
        driver.find_element(By.ID, "s-cantidad").clear()
        driver.find_element(By.ID, "s-cantidad").send_keys("2")
        
        driver.find_element(By.ID, "s-unidad").clear()
        driver.find_element(By.ID, "s-unidad").send_keys("metros")
        
        driver.find_element(By.ID, "s-minimo").clear()
        driver.find_element(By.ID, "s-minimo").send_keys("10")

        # 4. Ejecutar Acción
        driver.find_element(By.XPATH, "//button[contains(text(),'Registrar Insumo')]").click()

        # 5. Validación Esperada (Assert)
        # La forma más segura de validarlo visualmente es buscar que la fila creada contenga el texto "⚠️ Bajo"
        # que tu JavaScript inyecta en la tabla cuando cantidad <= stock_minimo
        xpath_alerta_tabla = "//td[text()='1']/following-sibling::td[contains(text(), '⚠️ Bajo')]"
        celda_alerta = wait.until(EC.presence_of_element_located((By.XPATH, xpath_alerta_tabla)))

        assert celda_alerta.is_displayed(), "La prueba falló: El sistema no mostró el indicador visual '⚠️ Bajo' en la tabla de stock."

    finally:
        driver.quit()