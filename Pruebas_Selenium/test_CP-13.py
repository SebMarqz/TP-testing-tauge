import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp13_buscar_pedido_por_fecha():
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
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr")))

        # Ingresar filtro de fecha estimada. 
        # Usamos un inyector JS para evitar problemas de locale con el input type="date"
        fecha_busqueda = "2026-05-25"
        driver.execute_script(f"document.getElementById('filtro-fecha').value = '{fecha_busqueda}';")
        
        # Click en Buscar
        driver.find_element(By.XPATH, "//div[@id='sec-pedidos']//button[text()='Buscar']").click()

        # Esperar a que la petición a la API termine y la tabla se refresque
        time.sleep(1)

        # Validar que todos los pedidos listados tengan la fecha buscada
        # En el nuevo HTML, la fecha estimada está en la 5ta columna (td[5])
        filas = driver.find_elements(By.XPATH, "//tbody[@id='tbody-pedidos']/tr")
        for fila in filas:
            fecha_celda = fila.find_element(By.XPATH, "./td[5]").text
            assert fecha_celda == fecha_busqueda, f"Se encontró un pedido con fecha diferente: {fecha_celda}"

    finally:
        driver.quit()