from Seguridad.Usuarios_json import cargar_usuarios, guardar_usuarios


def agregar_usuario():
    print("\n=== AGREGAR USUARIO ===")
    nombre_usuario = input("Usuario: ").strip()

    if not nombre_usuario:
        print("El usuario no puede estar vacio.")
        return

    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if usuario.get("usuario") == nombre_usuario:
            print("Ya existe un usuario con ese nombre.")
            return

    clave = input("Clave: ").strip()
    if not clave:
        print("La clave no puede estar vacia.")
        return

    rol = input("Rol (admin/usuario): ").strip().lower()
    if rol not in ("admin", "usuario"):
        rol = "usuario"

    usuarios.append(
        {
            "usuario": nombre_usuario,
            "clave": clave,
            "rol": rol,
        }
    )
    guardar_usuarios(usuarios)
    print("Usuario agregado correctamente.")
