from Seguridad.Usuarios_json import cargar_usuarios, guardar_usuarios


def modificar_usuario():
    print("\n=== MODIFICAR USUARIO ===")
    nombre_usuario = input("Usuario a modificar: ").strip()
    usuarios = cargar_usuarios()

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.get("usuario") == nombre_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("No existe un usuario con ese nombre.")
        return

    nuevo_nombre = input("Nuevo usuario (enter para mantener): ").strip()
    if nuevo_nombre and nuevo_nombre != nombre_usuario:
        for usuario in usuarios:
            if usuario.get("usuario") == nuevo_nombre:
                print("Ya existe un usuario con ese nombre.")
                return
        usuario_encontrado["usuario"] = nuevo_nombre

    nueva_clave = input("Nueva clave (enter para mantener): ").strip()
    if nueva_clave:
        usuario_encontrado["clave"] = nueva_clave

    nuevo_rol = input("Nuevo rol admin/usuario (enter para mantener): ").strip().lower()
    if nuevo_rol in ("admin", "usuario"):
        usuario_encontrado["rol"] = nuevo_rol

    guardar_usuarios(usuarios)
    print("Usuario modificado correctamente.")
