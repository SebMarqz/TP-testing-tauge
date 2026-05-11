from Usuario.Agregar_usuario import agregar_usuario
from Usuario.Modificar_usuario import modificar_usuario
from Usuario.Eliminar_usuario import eliminar_usuario


def menu_usuario():
    while True:
        print("\n=== MENÚ USUARIOS ===")
        print("1. Agregar usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("0. Volver")

        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            modificar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")