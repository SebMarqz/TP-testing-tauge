import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp06_modificar_pedido():
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

        # 1. Hacer click en "Edit" en la fila del Pedido ID 1
        btn_edit = driver.find_element(By.XPATH, "//tr[td[1][text()='1']]//button[contains(text(), 'Edit')]")
        btn_edit.click()

        # 2. Modificar la descripción en el formulario
        input_desc = driver.find_element(By.ID, "p-desc")
        input_desc.clear()
        nueva_descripcion = "Nueva descripcion"
        input_desc.send_keys(nueva_descripcion)

        # 3. Guardar los cambios
        driver.find_element(By.XPATH, "//div[@id='sec-pedidos']//button[contains(text(),'Guardar Pedido')]").click()

        # 4. Validar mensaje de éxito
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))
        assert "Pedido guardado" in mensaje.text

        # Esperar a que la tabla se recargue
        time.sleep(1)

        # 5. Validar que la tabla muestra la nueva descripción para el pedido ID 1
        # (La descripción está en la 3ra columna)
        fila_modificada = driver.find_element(By.XPATH, "//tr[td[1][text()='1']]")
        texto_desc_tabla = fila_modificada.find_element(By.XPATH, "./td[3]").text
        
        assert texto_desc_tabla == nueva_descripcion, "La modificación no se guardó/reflejó en la tabla"

    finally:
        driver.quit()