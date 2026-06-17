from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp10_visualizar_pedidos():
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

        # Ir a Pedidos y esperar que se listen elementos en la tabla
        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))
        
        # Esperar a que la tabla tenga al menos un `<select>` de estado, indicando que cargaron datos
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr td select")))

        # Validación esperada CP-10: Existen filas en la tabla
        filas_pedidos = driver.find_elements(By.XPATH, "//tbody[@id='tbody-pedidos']/tr")
        assert len(filas_pedidos) > 0, "No se están visualizando los pedidos en la tabla"

    finally:
        driver.quit()