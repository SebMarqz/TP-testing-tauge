from fastapi import APIRouter, HTTPException
from models import LoginModel
from database import usuarios_db

router = APIRouter()

@router.post("/login", tags=["Seguridad"])
def login(user: LoginModel):

    if user.username in usuarios_db:

        if usuarios_db[user.username]["password"] == user.password:

            return {
                "mensaje": "Login exitoso",
                "usuario": user.username,
                "rol": usuarios_db[user.username]["rol"],
                "token": f"fake-token-{user.username}"
            }

    raise HTTPException(
        status_code=401,
        detail="Credenciales inválidas"
    )
