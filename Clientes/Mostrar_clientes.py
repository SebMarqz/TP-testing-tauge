from Clientes.Clientes_json import cargar_clientes, mostrar_cliente


def mostrar_clientes():
    print("\n=== LISTADO DE CLIENTES ===")
    clientes = cargar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        mostrar_cliente(cliente)
        print("-" * 30)
