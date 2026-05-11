from Pedidos.Agregar_pedido import agregar_pedido
from Pedidos.Buscar_pedidos import buscar_pedido
from Pedidos.Modificar_pedido import modificar_pedido
from Pedidos.Eliminar_pedido import eliminar_pedido
from Pedidos.Mostrar_pedidos import mostrar_pedidos
from Pedidos.Estado_pedido import cambiar_estado_pedido
from Pedidos.Pago_pedidos import registrar_pago_pedido


def menu_pedidos():
    while True:
        print("\n=== MENU PEDIDOS ===")
        print("1. Mostrar pedidos")
        print("2. Agregar pedido")
        print("3. Buscar pedido")
        print("4. Modificar pedido")
        print("5. Cancelar pedido")
        print("6. Cambiar estado")
        print("7. Registrar pago")
        print("0. Volver")

        opcion = input("Ingrese opcion: ").strip()

        if opcion == "1":
            mostrar_pedidos()
        elif opcion == "2":
            agregar_pedido()
        elif opcion == "3":
            buscar_pedido()
        elif opcion == "4":
            modificar_pedido()
        elif opcion == "5":
            eliminar_pedido()
        elif opcion == "6":
            cambiar_estado_pedido()
        elif opcion == "7":
            registrar_pago_pedido()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
