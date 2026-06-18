from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp17_validar_cambio_estado_invalido():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Ajustar la ruta según el entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 1. Login con credenciales válidas
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")

        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")

        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 2. Esperar a que cargue la vista de la aplicación y la pestaña de Pedidos
        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))
        
        # Esperar a que la tabla cargue los pedidos (el select de estado)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbody-pedidos tr td select")))

        # 3. Ubicar el select del estado del pedido
        # Buscamos el select en la 5ta columna de la primera fila (asumiendo que es el pedido ID 1 en estado "Pendiente")
        estado_select_element = driver.find_element(By.XPATH, "//tbody[@id='tbody-pedidos']/tr[1]/td[5]/select")
        select = Select(estado_select_element)

        # 4. Intentar realizar la transición inválida (Pendiente -> Entregado)
        select.select_by_value("Entregado")

        # 5. Validación esperada CP-17: El sistema rechaza la transición y muestra un error
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        # Esperamos a que el cartel adquiera la clase de 'error' que asigna la función showMsg()
        wait.until(lambda d: "error" in mensaje.get_attribute("class"))

        # Verificamos que el mensaje es efectivamente de error
        assert "error" in mensaje.get_attribute("class")
        assert "Estado actualizado" not in mensaje.text # Opcional: garantizar que no diga éxito

    finally:
        driver.quit()