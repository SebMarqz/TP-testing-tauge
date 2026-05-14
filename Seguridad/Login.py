from API.api_client import login as api_login


def login():
    print('\n=== LOGIN ===')
    nombre_usuario=input('Usuario: ').strip()
    clave=input('Clave: ').strip()

    usuario=api_login(nombre_usuario,clave)

    if usuario:
        return {
            'usuario': usuario.get('usuario'),
            'rol': usuario.get('rol','usuario')
        }

    print('Usuario o clave incorrectos.')
    return None
