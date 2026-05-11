import json
from pathlib import Path


ARCHIVO_USUARIOS = Path(__file__).resolve().parent.parent / "Usuario" / "usuarios.json"
USUARIOS_INICIALES = [
    {
        "usuario": "admin",
        "clave": "admin",
        "rol": "admin",
    }
]


def cargar_usuarios():
    if not ARCHIVO_USUARIOS.exists():
        guardar_usuarios(USUARIOS_INICIALES)
        return USUARIOS_INICIALES.copy()

    try:
        with ARCHIVO_USUARIOS.open("r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except json.JSONDecodeError:
        usuarios = []

    if not isinstance(usuarios, list):
        usuarios = []

    if not usuarios:
        guardar_usuarios(USUARIOS_INICIALES)
        return USUARIOS_INICIALES.copy()

    return usuarios


def guardar_usuarios(usuarios):
    with ARCHIVO_USUARIOS.open("w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)


def buscar_usuario(nombre_usuario):
    for usuario in cargar_usuarios():
        if usuario.get("usuario") == nombre_usuario:
            return usuario

    return None
