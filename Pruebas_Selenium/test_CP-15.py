from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp15_estado_en_preparacion_a_listo():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Ajustar la ruta según el entorno
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
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr td select")))

        # Ubicar el select del estado para el Pedido con ID = 1
        estado_select_element = driver.find_element(By.XPATH, "//tr[td[1][text()='1']]/td[5]/select")
        select = Select(estado_select_element)

        # Transición: En preparacion -> Listo
        select.select_by_value("Listo")

        # Validación esperada CP-15
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))

        assert "Estado actualizado" in mensaje.text
        assert "success" in mensaje.get_attribute("class")

    finally:
        driver.quit()