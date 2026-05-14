from fastapi import APIRouter, HTTPException, Depends

from models import Usuario
from database import usuarios_db
from auth import verificar_usuario

router = APIRouter()

@router.post("/usuarios", tags=["Usuarios"])
def agregar_usuario(
    usuario: Usuario,
    user = Depends(verificar_usuario)
):

    if usuario.username in usuarios_db:

        raise HTTPException(
            status_code=400,
            detail="Usuario ya existe"
        )

    usuarios_db[usuario.username] = usuario.dict()

    return {
        "mensaje": "Usuario agregado"
    }

@router.put("/usuarios/{username}", tags=["Usuarios"])
def modificar_usuario(
    username: str,
    nuevo_usuario: Usuario,
    user = Depends(verificar_usuario)
):

    if username not in usuarios_db:

        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    usuarios_db[username] = nuevo_usuario.dict()

    return {
        "mensaje": "Usuario modificado"
    }

@router.delete("/usuarios/{username}", tags=["Usuarios"])
def eliminar_usuario(
    username: str,
    user = Depends(verificar_usuario)
):

    if username not in usuarios_db:

        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    del usuarios_db[username]

    return {
        "mensaje": "Usuario eliminado"
    }