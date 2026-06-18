from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp32_acceso_empleado_restringido():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 2. Ingreso de Datos (Precondición: Usuario empleado existente)
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("empleado")
        
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123456")

        # 3. Ejecutar Acción
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 4. Validación Esperada (Assert)
        # Esperamos a que la pantalla principal de la app cargue
        app_view = wait.until(EC.presence_of_element_located((By.ID, "view-app")))
        wait.until(lambda d: "hidden" not in app_view.get_attribute("class"))

        # Verificamos que la pestaña de usuarios NO sea visible para el empleado
        tab_usuarios = driver.find_element(By.ID, "tab-usuarios")
        assert not tab_usuarios.is_displayed(), "La prueba falló: El empleado tiene acceso a la pestaña de Usuarios (Admin)."

    finally:
        driver.quit()