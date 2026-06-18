from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pathlib import Path

def test_cp35_modificar_usuario_existente():
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

        # 3. Hacer clic en el botón de Editar (✏️) del usuario 'empleado1'
        xpath_boton_editar = "//td[text()='empleado1']/following-sibling::td[contains(@class, 'actions-cell')]/button[contains(@class, 'btn-primary')]"
        boton_editar = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_boton_editar)))
        boton_editar.click()

        # 4. Ingresar nueva contraseña (Datos CP-35)
        # El username se bloquea automáticamente por JS al editar, solo cambiamos contraseña y rol
        driver.find_element(By.ID, "u-password").clear()
        driver.find_element(By.ID, "u-password").send_keys("nueva123")
        
        select_rol = Select(driver.find_element(By.ID, "u-rol"))
        select_rol.select_by_value("Empleado")

        # 5. Ejecutar Acción
        driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Usuario')]").click()

        # 6. Validación Esperada (Assert)
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        clases_mensaje = mensaje.get_attribute("class")
        assert "success" in clases_mensaje and "Usuario guardado" in mensaje.text, "La prueba falló: El usuario no fue actualizado correctamente."

    finally:
        driver.quit()