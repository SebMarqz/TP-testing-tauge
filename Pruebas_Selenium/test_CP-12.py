import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp12_buscar_pedido_por_estado_listo():
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

        # Seleccionar filtro estado = Listo y buscar
        filtro_estado = Select(driver.find_element(By.ID, "filtro-estado"))
        filtro_estado.select_by_value("Listo")
        driver.find_element(By.XPATH, "//div[@id='sec-pedidos']//button[text()='Buscar']").click()

        time.sleep(1)

        # Validar que todos los pedidos en la tabla tengan el select de estado en "Listo"
        filas = driver.find_elements(By.XPATH, "//tbody[@id='tbody-pedidos']/tr")
        for fila in filas:
            select_estado_celda = fila.find_element(By.XPATH, "./td[5]/select")
            assert select_estado_celda.get_attribute("value") == "Listo", "Se encontró un pedido con un estado diferente a Listo"

    finally:
        driver.quit()