from Menus.Menu_clientes import menu_clientes
from Menus.Menu_pedidos import menu_pedidos
from Menus.Menu_usuario import menu_usuario
from Menus.Menu_stock import menu_stock

def menu_general(usuario_logueado):
    while True:
        print("\n=== MENÚ GENERAL - TAUGE ===")
        print("1. Clientes")
        print("2. Pedidos")
        print("3. Stock")

        if usuario_logueado.get("rol") == "admin":
            print("4. Usuarios")

        print("0. Salir")

        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_pedidos()

        elif opcion == "3":
            menu_stock()

        elif opcion == "4" and usuario_logueado.get("rol") == "admin":
            menu_usuario()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

