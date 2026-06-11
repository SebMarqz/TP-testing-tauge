from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path

def test_cp24_entregar_pedido_sin_pago():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación y Login
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 2. Asegurar que estamos en Pedidos
        wait.until(EC.element_to_be_clickable((By.ID, "tab-pedidos"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "sec-pedidos")))

        # 3. Buscar el dropdown de Estado (Columna 5) y cambiarlo a "Entregado"
        xpath_select_estado = "//td[text()='1']/parent::tr/td[5]/select"
        select_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_select_estado)))
        
        Select(select_element).select_by_value("Entregado")

        # 4. Validación Esperada (Assert)
        # Esperamos el cartel de éxito disparado por el catch de la función JS
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))
        
        # Opcional: Validamos que la tabla recargada muestre la opción correcta
        # Re-buscamos el elemento porque el DOM se recargó al hacer onchange
        select_actualizado = wait.until(EC.presence_of_element_located((By.XPATH, xpath_select_estado)))
        valor_actual = Select(select_actualizado).first_selected_option.get_attribute("value")
        
        assert valor_actual == "Entregado", f"La prueba falló: El estado quedó en '{valor_actual}' en lugar de 'Entregado'."

    finally:
        driver.quit()