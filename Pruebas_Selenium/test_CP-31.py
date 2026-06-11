from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp31_login_administrador_acceso_completo():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 2. Ingreso de Datos (Admin)
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")

        # 3. Ejecutar Acción
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 4. Validación Esperada (Assert)
        app_view = wait.until(EC.presence_of_element_located((By.ID, "view-app")))
        wait.until(lambda d: "hidden" not in app_view.get_attribute("class"))

        # Verificamos que la pestaña de usuarios SÍ sea visible
        tab_usuarios = driver.find_element(By.ID, "tab-usuarios")
        assert tab_usuarios.is_displayed(), "La prueba falló: El administrador no puede ver la pestaña de Usuarios."

    finally:
        driver.quit()