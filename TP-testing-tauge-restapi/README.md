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

## Windows CMD

```bash
venv\Scripts\activate
```

## Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
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

# 5. Ejecutar el proyecto

```bash
uvicorn Main:app --reload
```

---

# 6. Abrir Swagger

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

---

# 7. Login de prueba

Usuario:

```text
admin
```

Contraseña:

```text
123
```

---

# 8. Autorizar endpoints

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

En la seccion de auth pegar el token recibido por ej:

```text
fake-token-admin
```
---