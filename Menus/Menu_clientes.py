from Clientes.Agregar_cliente import agregar_cliente
from Clientes.Buscar_cliente import buscar_cliente
from Clientes.Modificar_cliente import modificar_cliente
from Clientes.Eliminar_cliente import eliminar_cliente
from Clientes.Mostrar_clientes import mostrar_clientes


def menu_clientes():
    while True:
        print("\n=== MENÚ CLIENTES ===")
        print("1. Mostrar clientes")
        print("2. Agregar cliente")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("0. Volver")

        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")