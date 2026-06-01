from fastapi import APIRouter, HTTPException, Depends
from models import Usuario
from database import usuarios_db, guardar_usuarios
from auth import verificar_usuario

router = APIRouter()

@router.get("/usuarios", tags=["Usuarios"])
def mostrar_usuarios(user = Depends(verificar_usuario)):
    
    if user.get("rol") != "Administrador":
        raise HTTPException(
            status_code=403, 
            detail="Acceso denegado. Solo los administradores pueden ver la lista de usuarios."
        )
    
    # usuarios_db es un diccionario, así que devolvemos solo sus valores en formato de lista
    return list(usuarios_db.values())

@router.post("/usuarios", tags=["Usuarios"])
def agregar_usuario(usuario: Usuario, user = Depends(verificar_usuario)):
    if user.get("rol") != "Administrador":
        raise HTTPException(
            status_code=403, 
            detail="Acceso denegado. Solo los administradores pueden crear usuarios."
        )

    if usuario.username in usuarios_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    
    usuarios_db[usuario.username] = usuario.dict()
    guardar_usuarios()
    return {"mensaje": "Usuario agregado"}

@router.put("/usuarios/{username}", tags=["Usuarios"])
def modificar_usuario(username: str, nuevo_usuario: Usuario, user = Depends(verificar_usuario)):
    if user.get("rol") != "Administrador":
        raise HTTPException(
            status_code=403, 
            detail="Acceso denegado. Solo los administradores pueden modificar usuarios."
        )

    if username not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuarios_db[username] = nuevo_usuario.dict()
    guardar_usuarios()
    return {"mensaje": "Usuario modificado"}

@router.delete("/usuarios/{username}", tags=["Usuarios"])
def eliminar_usuario(username: str, user = Depends(verificar_usuario)):
    if user.get("rol") != "Administrador":
        raise HTTPException(
            status_code=403, 
            detail="Acceso denegado. Solo los administradores pueden eliminar usuarios."
        )

    if username not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if username == "admin":
        raise HTTPException(status_code=400, detail="No se puede eliminar el usuario administrador por defecto")
        
    del usuarios_db[username]
    guardar_usuarios()
    return {"mensaje": "Usuario eliminado"}