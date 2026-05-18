# TP_TESTING_TAUGE

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TP_TESTING_TAUGE.git
```

Entrar a la carpeta:

```bash
cd TP_TESTING_TAUGE
```

---

# 2. Crear entorno virtual (venv)

## Windows

```bash
python -m venv venv
```

## Linux / macOS

```bash
python3 -m venv venv
```

---

# 3. Activar entorno virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux / macOS

```bash
source venv/bin/activate
```

---

# 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 5. Ejecutar la API REST

```bash
cd restapi
uvicorn Main:app --reload
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

---

# 6. Ejecutar el cliente de terminal

Abrir una segunda terminal, activar nuevamente el venv y ejecutar:

```bash
python ClienteTerminal.py
```

El cliente de terminal se conectará automáticamente a la REST API mediante requests HTTP.

---

# 7. Abrir Swagger

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

---

# 8. Login de prueba

Usuario:

```text
admin
```

Contraseña:

```text
123
```

---

# 9. Autorizar endpoints

## Hacer login

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

---

## Usar token

En la sección de auth pegar el token recibido, por ejemplo:

```text
fake-token-admin
```

---

# 10. Verificar integración terminal + API

Con la API ejecutándose, usar el programa de terminal para:

* Mostrar clientes
* Agregar clientes
* Buscar clientes
* Modificar clientes
* Eliminar clientes

Mientras se usa el cliente de terminal, en la consola de uvicorn aparecerán requests como:

```text
POST /login
GET /clientes
POST /clientes
PUT /clientes/1
DELETE /clientes/1
```

Eso confirma que el programa de terminal está consumiendo la REST API correctamente.
