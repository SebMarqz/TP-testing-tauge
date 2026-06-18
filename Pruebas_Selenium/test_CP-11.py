import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp11_buscar_pedido_por_cliente():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # Login
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr")))

        # Ingresar filtro cliente_id = 1 y buscar
        driver.find_element(By.ID, "filtro-cliente").send_keys("1")
        driver.find_element(By.XPATH, "//div[@id='sec-pedidos']//button[text()='Buscar']").click()

        # Esperar a que la tabla se refresque
        time.sleep(1)

        # Validar que todos los resultados mostrados correspondan al cliente_id 1 (Columna 2)
        filas = driver.find_elements(By.XPATH, "//tbody[@id='tbody-pedidos']/tr")
        for fila in filas:
            cliente_id_celda = fila.find_element(By.XPATH, "./td[2]").text
            assert cliente_id_celda == "1", f"Se encontró un pedido de un cliente distinto: {cliente_id_celda}"

    finally:
        driver.quit()