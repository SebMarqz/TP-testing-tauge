import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp05_generar_id_automatico():
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
        
        # Datos de prueba para el nuevo pedido
        desc_test = "Tarjetas personales"
        driver.find_element(By.ID, "p-cliente").send_keys("1")
        driver.find_element(By.ID, "p-desc").send_keys(desc_test)
        driver.find_element(By.ID, "p-tipo").send_keys("Diseño")
        
        # Inyectar fecha de prueba
        driver.execute_script("document.getElementById('p-fecha').value = '2026-05-28';")

        # Guardar pedido
        driver.find_element(By.XPATH, "//div[@id='sec-pedidos']//button[contains(text(),'Guardar Pedido')]").click()

        # Validación 1: Mensaje de éxito
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))
        assert "Pedido guardado" in mensaje.text

        # Esperar a que la tabla se recargue
        time.sleep(1)

        # Validación 2: Buscar el pedido en la tabla por la descripción y verificar que tiene un ID numérico válido (> 0)
        # La descripción está en la 3ra columna
        fila_creada = driver.find_element(By.XPATH, f"//tbody[@id='tbody-pedidos']/tr[td[3][text()='{desc_test}']]")
        id_asignado = fila_creada.find_element(By.XPATH, "./td[1]").text
        
        assert id_asignado.isdigit(), "El ID asignado no es un número"
        assert int(id_asignado) > 0, "El sistema no generó un ID automático válido"

    finally:
        driver.quit()