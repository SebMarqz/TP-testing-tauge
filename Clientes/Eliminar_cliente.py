from Clientes.Clientes_json import (
    buscar_cliente_por_id,
    cargar_clientes,
    guardar_clientes,
)


def eliminar_cliente():
    print("\n=== ELIMINAR CLIENTE ===")
    cliente_id = input("ID del cliente: ").strip()

    if not cliente_id.isdigit():
        print("El ID debe ser numerico.")
        return

    clientes = cargar_clientes()
    cliente = buscar_cliente_por_id(clientes, int(cliente_id))

    if not cliente:
        print("No existe un cliente con ese ID.")
        return

    clientes.remove(cliente)
    guardar_clientes(clientes)
    print("Cliente eliminado correctamente.")
