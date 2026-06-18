from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path

def test_cp22_marcar_pedido_pagado():
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

        # 3. Buscar el dropdown de Pago (Columna 6) y cambiarlo a "Pagado"
        xpath_select_pago = "//td[text()='1']/parent::tr/td[6]/select"
        select_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_select_pago)))
        
        Select(select_element).select_by_value("Pagado")

        # 4. Validación Esperada (Assert)
        mensaje = wait.until(EC.presence_of_element_located((By.ID, "global-msg")))
        wait.until(lambda d: "success" in mensaje.get_attribute("class"))
        
        select_actualizado = wait.until(EC.presence_of_element_located((By.XPATH, xpath_select_pago)))
        valor_actual = Select(select_actualizado).first_selected_option.get_attribute("value")
        
        assert valor_actual == "Pagado", f"La prueba falló: El pago quedó en '{valor_actual}' en lugar de 'Pagado'."

    finally:
        driver.quit()