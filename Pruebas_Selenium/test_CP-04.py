from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp04_registrar_pedido_sin_fecha():
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

        wait.until(
            EC.presence_of_element_located((By.ID, "tab-pedidos"))
        )

        # Datos CP-04
        driver.find_element(By.ID, "p-cliente").clear()
        driver.find_element(By.ID, "p-cliente").send_keys("1")

        driver.find_element(By.ID, "p-desc").clear()
        driver.find_element(By.ID, "p-desc").send_keys("Banner publicitario")

        driver.find_element(By.ID, "p-tipo").clear()
        driver.find_element(By.ID, "p-tipo").send_keys("Impresion")

        # Fecha vacía
        driver.find_element(By.ID, "p-fecha").clear()

        driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Guardar Pedido')]"
        ).click()

        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )

        clases = mensaje.get_attribute("class")

        assert "error" in clases

    finally:
        driver.quit()