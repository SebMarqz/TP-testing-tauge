from Seguridad.Usuarios_json import cargar_usuarios, guardar_usuarios


def eliminar_usuario():
    print("\n=== ELIMINAR USUARIO ===")
    nombre_usuario = input("Usuario a eliminar: ").strip()
    usuarios = cargar_usuarios()

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.get("usuario") == nombre_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("No existe un usuario con ese nombre.")
        return

    admins = [usuario for usuario in usuarios if usuario.get("rol") == "admin"]
    if usuario_encontrado.get("rol") == "admin" and len(admins) == 1:
        print("No se puede eliminar el ultimo usuario administrador.")
        return

    usuarios.remove(usuario_encontrado)
    guardar_usuarios(usuarios)
    print("Usuario eliminado correctamente.")
