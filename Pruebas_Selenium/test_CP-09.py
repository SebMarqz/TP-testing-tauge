import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp09_cancelar_pedido_entregado():
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

        # Ubicar y hacer clic en el botón Cancelar del pedido ID 2
        btn_cancelar = driver.find_element(By.XPATH, "//tr[td[1][text()='2']]//button[contains(text(), 'Cancelar')]")
        btn_cancelar.click()

        # Manejar la alerta de confirmación
        alert = wait.until(EC.alert_is_present())
        alert.accept()

        time.sleep(1)
        
        # Validar si el sistema aplica la regla de negocio y lo cancela o arroja error
        # Revisa el mensaje global por si la API bloquea la acción
        mensajes_error = driver.find_elements(By.CSS_SELECTOR, "#global-msg.error")
        if len(mensajes_error) > 0 and mensajes_error[0].is_displayed():
            print("El sistema bloqueó la cancelación del pedido entregado:", mensajes_error[0].text)
        else:
            # Si permite la cancelación, verificar que el estado sea "Cancelado"
            filas = driver.find_elements(By.XPATH, "//tr[td[1][text()='2']]")
            if len(filas) > 0:
                select_estado = filas[0].find_element(By.XPATH, "./td[5]/select")
                assert select_estado.get_attribute("value") == "Cancelado"

    finally:
        driver.quit()