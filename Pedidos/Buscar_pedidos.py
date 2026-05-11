from Pedidos.Pedidos_json import cargar_pedidos, mostrar_resumen_pedido


def buscar_pedido():
    print("\n=== BUSCAR PEDIDO ===")
    print("1. Por cliente")
    print("2. Por estado")
    print("3. Por fecha estimada")
    opcion = input("Ingrese opcion: ").strip()

    pedidos = cargar_pedidos()
    resultados = []

    if opcion == "1":
        cliente = input("Cliente: ").strip().lower()
        resultados = [
            pedido for pedido in pedidos if cliente in pedido.get("cliente", "").lower()
        ]
    elif opcion == "2":
        estado = input("Estado: ").strip().lower()
        resultados = [
            pedido for pedido in pedidos if estado == pedido.get("estado", "").lower()
        ]
    elif opcion == "3":
        fecha = input("Fecha estimada (dd/mm/aaaa): ").strip()
        resultados = [
            pedido for pedido in pedidos if fecha == pedido.get("fecha_estimada", "")
        ]
    else:
        print("Opcion invalida.")
        return

    if not resultados:
        print("No se encontraron pedidos.")
        return

    for pedido in resultados:
        mostrar_resumen_pedido(pedido)
        print("-" * 30)
