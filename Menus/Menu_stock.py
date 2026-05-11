from Stock.Mostrar_stock import mostrar_stock
from Stock.Agregar_stock import agregar_stock
from Stock.Quitar_stock import quitar_stock


def menu_stock():
    while True:
        print("\n=== MENU STOCK ===")
        print("1. Mostrar stock")
        print("2. Agregar stock")
        print("3. Quitar stock")
        print("0. Volver")

        opcion = input("Ingrese opcion: ").strip()

        if opcion == "1":
            mostrar_stock()
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            quitar_stock()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
