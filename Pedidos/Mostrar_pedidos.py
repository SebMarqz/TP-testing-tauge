from Pedidos.Pedidos_json import cargar_pedidos, mostrar_resumen_pedido


def mostrar_pedidos():
    print("\n=== LISTADO DE PEDIDOS ===")
    pedidos = cargar_pedidos()

    if not pedidos:
        print("No hay pedidos registrados.")
        return

    for pedido in pedidos:
        mostrar_resumen_pedido(pedido)
        print("-" * 30)
