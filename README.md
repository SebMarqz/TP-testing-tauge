# TP_TESTING_TAUGE

## 1. Clonar el repositorio

```bash
git clone https://github.com/SebMarqz/TP-testing-tauge.git
git checkout integrado
```

Entrar a la carpeta:

```bash
cd TP_TESTING_TAUGE
```

---

## 2. Crear entorno virtual (venv)

### Windows

```bash
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## 3. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5. Ejecutar la API REST

```bash
cd restapi
uvicorn Main:app --reload
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

---

## 6. Abrir Swagger

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

---

## 7. Login de prueba

Usuario:

```text
admin
```

Contraseña:

```text
123
```

---

## 8. Autorizar endpoints (Swagger)

### Hacer login

Endpoint:

```http
POST /login
```

Body:

```json
{
  "username": "admin",
  "password": "123"
}
```

La API devuelve un token.

### Usar token

En la sección de auth de Swagger, pegar el token recibido, por ejemplo:

```text
fake-token-admin
```

---

## 9. Ejecutar pruebas automatizadas (Selenium + Pytest)

Para ejecutar los casos de prueba End-to-End (E2E) sobre la interfaz web, es necesario **tener la API REST en ejecución** (Paso 5) en una terminal.

Abrir una **segunda terminal**, activar nuevamente el entorno virtual (Paso 3) y navegar a la carpeta de las pruebas:

```bash
cd Pruebas_Selenium
```

Para ejecutar todos los casos de prueba de la carpeta:

```bash
pytest
```

Para ejecutar un caso de prueba en específico (por ejemplo, el CP-01):

```bash
pytest CP-01.py
```