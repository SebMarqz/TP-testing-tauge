from Seguridad.Usuarios_json import buscar_usuario


def login():
    print("\n=== LOGIN ===")
    nombre_usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()
    usuario = buscar_usuario(nombre_usuario)

    if usuario and usuario.get("clave") == clave:
        return {
            "usuario": usuario.get("usuario"),
            "rol": usuario.get("rol", "usuario"),
        }

    print("Usuario o clave incorrectos.")

    return None
