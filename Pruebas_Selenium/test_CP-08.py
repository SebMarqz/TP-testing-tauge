import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp08_cancelar_pedido():
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

        # Ir a Pedidos y esperar carga
        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr")))

        # Ubicar y hacer clic en el botón Cancelar del pedido ID 1
        btn_cancelar = driver.find_element(By.XPATH, "//tr[td[1][text()='1']]//button[contains(text(), 'Cancelar')]")
        btn_cancelar.click()

        # Manejar la alerta de confirmación
        alert = wait.until(EC.alert_is_present())
        alert.accept()

        # Esperar un momento a que la API responda y la tabla se actualice
        time.sleep(1)

        # Validación: El pedido debe pasar a estado "Cancelado" 
        # (Dependiendo de la API, la fila se actualiza o desaparece, verificamos que si existe, su estado sea Cancelado)
        filas = driver.find_elements(By.XPATH, "//tr[td[1][text()='1']]")
        if len(filas) > 0:
            select_estado = filas[0].find_element(By.XPATH, "./td[5]/select")
            assert select_estado.get_attribute("value") == "Cancelado"

    finally:
        driver.quit()