from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path

def test_cp37_crear_usuario_sin_contrasena():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 2. Login (Precondición: Usuario administrador logueado)
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # 3. Navegar a la pestaña de Usuarios (Admin)
        wait.until(EC.element_to_be_clickable((By.ID, "tab-usuarios"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "sec-usuarios")))

        # 4. Ingreso de Datos de Prueba CP-37 (IDs exactos del HTML)
        driver.find_element(By.ID, "u-username").clear()
        driver.find_element(By.ID, "u-username").send_keys("usuario1")
        
        # Selección del rol mediante la clase Select
        select_rol = Select(driver.find_element(By.ID, "u-rol"))
        select_rol.select_by_value("Empleado")
        
        # Clave del CP-37: Dejar la contraseña vacía
        driver.find_element(By.ID, "u-password").clear()

        # 5. Ejecutar Acción (Guardar Usuario)
        driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Usuario')]").click()

        # 6. Validación Esperada (Assert)
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        clases_mensaje = mensaje.get_attribute("class")
        assert "error" in clases_mensaje, f"La prueba falló: El sistema no validó la obligatoriedad de la contraseña. Clases actuales: {clases_mensaje}"

    finally:
        driver.quit()