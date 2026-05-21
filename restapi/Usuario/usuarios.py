from fastapi import APIRouter, HTTPException, Depends
from models import Usuario
from database import usuarios_db, guardar_usuarios
from auth import verificar_usuario

router = APIRouter()

@router.post("/usuarios", tags=["Usuarios"])
def agregar_usuario(usuario: Usuario, user = Depends(verificar_usuario)):
    if usuario.username in usuarios_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    
    nuevo_user_dict = usuario.dict()
    nuevo_user_dict["rol"] = "Administrador"
    
    usuarios_db[usuario.username] = nuevo_user_dict
    guardar_usuarios()
    return {"mensaje": "Usuario agregado"}

@router.put("/usuarios/{username}", tags=["Usuarios"])
def modificar_usuario(username: str, nuevo_usuario: Usuario, user = Depends(verificar_usuario)):
    usuarios_db[username] = nuevo_usuario.dict()
    guardar_usuarios()
    return {"mensaje": "Usuario modificado"}

@router.delete("/usuarios/{username}", tags=["Usuarios"])
def eliminar_usuario(username: str, user = Depends(verificar_usuario)):
    if username == "admin":
        raise HTTPException(status_code=400, detail="No se puede eliminar el usuario administrador por defecto")
        
    if username in usuarios_db:
        del usuarios_db[username]
        
    guardar_usuarios()
    return {"mensaje": "Usuario eliminado"}