from Seguridad.Usuarios_json import cargar_usuarios, guardar_usuarios
from Seguridad.Validacion import validar_texto_obligatorio


def agregar_usuario():
    print("\n=== AGREGAR USUARIO ===")
    nombre_usuario = input("Usuario: ").strip()

    if not validar_texto_obligatorio(nombre_usuario, "Usuario"):
        return

    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if usuario.get("usuario") == nombre_usuario:
            print("Ya existe un usuario con ese nombre.")
            return

    clave = input("Clave: ").strip()
    if not validar_texto_obligatorio(clave, "Clave"):
        return

    rol = input("Rol (admin/usuario): ").strip().lower()
    if rol not in ("admin", "usuario"):
        print("Rol invalido. Use admin o usuario.")
        return

    usuarios.append(
        {
            "usuario": nombre_usuario,
            "clave": clave,
            "rol": rol,
        }
    )
    guardar_usuarios(usuarios)
    print("Usuario agregado correctamente.")
