from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp29_login_invalido():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 2. Ingreso de Datos (Contraseña incorrecta)
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("incorrecta")

        # 3. Ejecutar Acción
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 4. Validación Esperada (Assert)
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        wait.until(lambda d: "error" in mensaje.get_attribute("class") or "hidden" not in mensaje.get_attribute("class"))
        
        clases_mensaje = mensaje.get_attribute("class")
        assert "error" in clases_mensaje, f"La prueba falló: No se mostró error al ingresar contraseña incorrecta. Clases: {clases_mensaje}"

    finally:
        driver.quit()