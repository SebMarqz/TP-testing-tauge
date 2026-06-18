from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path

def test_cp33_crear_usuario_administrador():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno y Login
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 2. Navegar a Usuarios
        wait.until(EC.element_to_be_clickable((By.ID, "tab-usuarios"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "sec-usuarios")))

        # 3. Ingresar datos del nuevo administrador (Datos CP-33)
        driver.find_element(By.ID, "u-username").clear()
        driver.find_element(By.ID, "u-username").send_keys("nuevoadmin")
        
        driver.find_element(By.ID, "u-password").clear()
        driver.find_element(By.ID, "u-password").send_keys("admin123")
        
        select_rol = Select(driver.find_element(By.ID, "u-rol"))
        select_rol.select_by_value("Administrador")

        # 4. Ejecutar Acción
        driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Usuario')]").click()

        # 5. Validación Esperada (Assert)
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        clases_mensaje = mensaje.get_attribute("class")
        assert "success" in clases_mensaje and "Usuario guardado" in mensaje.text, "La prueba falló: El administrador no fue creado correctamente."

    finally:
        driver.quit()