from Menus.Menu_general import menu_general
from Seguridad.Login import login


def menu_login():
    usuario = login()
    if usuario:
        menu_general(usuario)
    else:
        print("No se pudo iniciar sesion.")
