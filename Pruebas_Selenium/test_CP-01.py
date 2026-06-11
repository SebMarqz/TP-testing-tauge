from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp01_registrar_pedido():
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

        # Ir a Pedidos
        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))

        # Datos de prueba CP-01
        driver.find_element(By.ID, "p-cliente").send_keys("1")
        driver.find_element(By.ID, "p-desc").send_keys("Banner publicitario")
        driver.find_element(By.ID, "p-tipo").send_keys("Impresion")
        driver.find_element(By.ID, "p-fecha").send_keys("2026-06-30")

        driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Pedido')]").click()

        # Validación esperada CP-01
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )

        assert "Pedido guardado" in mensaje.text

    finally:
        driver.quit()