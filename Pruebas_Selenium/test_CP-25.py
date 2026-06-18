from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def test_cp25_visualizar_stock():
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

        # 2. Navegar a Stock
        wait.until(EC.element_to_be_clickable((By.ID, "tab-stock"))).click()
        
        # 3. Validación Esperada (Assert)
        # Validamos que la sección de stock pierda la clase 'hidden' y sea visible en pantalla
        sec_stock = wait.until(EC.presence_of_element_located((By.ID, "sec-stock")))
        wait.until(lambda d: "hidden" not in sec_stock.get_attribute("class"))
        
        # Con verificar que la sección principal esté visible es suficiente para dar el caso por exitoso
        assert sec_stock.is_displayed(), "La prueba falló: No se pudo visualizar el panel de stock."

    finally:
        driver.quit()