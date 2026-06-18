from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


def test_cp20_modificar_cliente():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # ==========================================
        # 1. Login
        # ==========================================
        html_path = Path(__file__).parent.parent / "index.html"
        driver.get(html_path.resolve().as_uri())

        usuario = wait.until(
            EC.presence_of_element_located((By.ID, "login-user"))
        )
        usuario.clear()
        usuario.send_keys("admin")

        password = driver.find_element(By.ID, "login-pass")
        password.clear()
        password.send_keys("123")

        driver.find_element(
            By.CSS_SELECTOR,
            "#view-login button"
        ).click()

        # Esperar que aparezca la aplicación
        wait.until(
            EC.visibility_of_element_located((By.ID, "view-app"))
        )

        # ==========================================
        # 2. Ir a Clientes
        # ==========================================
        wait.until(
            EC.element_to_be_clickable((By.ID, "tab-clientes"))
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "sec-clientes"))
        )

        # Esperar que cargue la tabla
        wait.until(
            lambda d: len(
                d.find_elements(
                    By.XPATH,
                    "//tbody[@id='tbody-clientes']/tr"
                )
            ) > 0
        )

        # ==========================================
        # 3. Editar cliente con ID = 1
        # ==========================================
        xpath_btn_editar = (
            "//tbody[@id='tbody-clientes']"
            "//tr[td[1]='1']"
            "//button[contains(@class,'btn-primary')]"
        )

        boton_editar = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_btn_editar))
        )

        boton_editar.click()

        # Verificar que se abrió el cliente correcto
        campo_id = wait.until(
            EC.presence_of_element_located((By.ID, "c-id"))
        )

        assert campo_id.get_attribute("value") == "1", \
            "No se abrió el cliente con ID 1"

        # ==========================================
        # 4. Modificar teléfono
        # ==========================================
        telefono = driver.find_element(By.ID, "c-telefono")
        telefono.clear()
        telefono.send_keys("1199988877")

        # ==========================================
        # 5. Guardar cambios
        # ==========================================
        boton_guardar = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(text(),'Guardar Cliente')]"
                )
            )
        )

        boton_guardar.click()

        # ==========================================
        # 6. Validar mensaje de éxito
        # ==========================================
        mensaje = wait.until(
            EC.visibility_of_element_located((By.ID, "global-msg"))
        )

        assert "success" in mensaje.get_attribute("class"), \
            "No apareció mensaje de éxito"

        assert "Cliente guardado" in mensaje.text, \
            "Mensaje incorrecto"

        # ==========================================
        # 7. Validar actualización en la tabla
        # ==========================================
        wait.until(
            EC.text_to_be_present_in_element(
                (
                    By.XPATH,
                    "//tbody[@id='tbody-clientes']//tr[td[1]='1']/td[3]"
                ),
                "1199988877"
            )
        )

        telefono_actualizado = driver.find_element(
            By.XPATH,
            "//tbody[@id='tbody-clientes']//tr[td[1]='1']/td[3]"
        ).text

        assert telefono_actualizado == "1199988877", \
            "El teléfono no fue actualizado"

    finally:
        driver.quit()