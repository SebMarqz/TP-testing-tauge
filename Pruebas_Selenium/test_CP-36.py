from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp36_eliminar_usuario_existente():
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

        # 4. Ejecutar Acción
        # NOTA: Esta prueba asume que la precondición se cumple y "empleado1" ya existe en la tabla.
        # Buscamos el botón de eliminar específicamente en la fila que contiene el texto "empleado1"
        xpath_boton_eliminar = "//td[text()='empleado1']/following-sibling::td[contains(@class, 'actions-cell')]/button[contains(@class, 'btn-danger')]"
        
        boton_eliminar = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_boton_eliminar)))
        boton_eliminar.click()

        # Manejar el confirm() nativo de JavaScript para aceptar la eliminación
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        # 5. Validación Esperada (Assert)
        # Como no hay cartel verde, esperamos hasta que la celda con "empleado1" desaparezca del DOM
        xpath_celda_empleado = "//td[text()='empleado1']"
        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_celda_empleado)))
        
        # Comprobación final por seguridad
        usuarios_en_tabla = driver.find_elements(By.XPATH, xpath_celda_empleado)
        assert len(usuarios_en_tabla) == 0, "La prueba falló: El usuario 'empleado1' no fue eliminado de la tabla."

    finally:
        driver.quit()