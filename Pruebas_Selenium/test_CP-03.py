from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp03_registrar_pedido_sin_descripcion():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Preparación del entorno
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        # 2. Login (Precondición: Usuario logueado)
        driver.find_element(By.ID, "login-user").clear()
        driver.find_element(By.ID, "login-user").send_keys("admin")
        driver.find_element(By.ID, "login-pass").clear()
        driver.find_element(By.ID, "login-pass").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "#view-login button").click()

        # Esperar a que cargue la interfaz principal
        wait.until(EC.presence_of_element_located((By.ID, "tab-pedidos")))

        # 3. Ingreso de Datos de Prueba CP-03
        
        # Cliente ID: 1
        driver.find_element(By.ID, "p-cliente").clear()
        driver.find_element(By.ID, "p-cliente").send_keys("1")
        
        # CLAVE DEL CP-03: Limpiamos la descripción y la dejamos VACÍA
        driver.find_element(By.ID, "p-desc").clear()
        # (No usamos .send_keys() aquí intencionalmente)
        
        # Tipo de Trabajo: Impresion
        driver.find_element(By.ID, "p-tipo").clear()
        driver.find_element(By.ID, "p-tipo").send_keys("Impresion")
        
        # Fecha Estimada: 2026-06-05
        driver.find_element(By.ID, "p-fecha").clear()
        driver.find_element(By.ID, "p-fecha").send_keys("2026-06-05")

        # Intencionalmente omitimos interactuar con "p-insumos"

        # 4. Ejecutar Acción
        driver.find_element(By.XPATH, "//button[contains(text(),'Guardar Pedido')]").click()

        # 5. Validación Esperada (Assert)
        # El documento dice: "El sistema impide registrar el pedido". 
        # Por lo tanto, esperamos que salte el cartel rojo de error.
        mensaje = wait.until(
            EC.presence_of_element_located((By.ID, "global-msg"))
        )
        
        clases_mensaje = mensaje.get_attribute("class")
        assert "error" in clases_mensaje, f"La prueba falló: El sistema no impidió el registro ni mostró error. Clases actuales: {clases_mensaje}"

    finally:
        driver.quit()