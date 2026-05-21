import logging
from fastapi import APIRouter, HTTPException
from models import LoginModel
from database import usuarios_db

router = APIRouter()
logger = logging.getLogger("Seguridad") # Logger para este módulo

@router.post("/login", tags=["Seguridad"])
def login(user: LoginModel):
    logger.info(f"Intento de login para el usuario: '{user.username}'")

    if user.username in usuarios_db:
        if usuarios_db[user.username]["password"] == user.password:
            logger.info(f"Login exitoso. Usuario '{user.username}' autenticado correctamente.")
            return {
                "mensaje": "Login exitoso",
                "usuario": user.username,
                "rol": usuarios_db[user.username]["rol"],
                "token": f"fake-token-{user.username}"
            }

    # Si llega acá es porque falló
    logger.warning(f"Credenciales inválidas para el usuario: '{user.username}'")
    raise HTTPException(
        status_code=401,
        detail="Credenciales inválidas"
    )