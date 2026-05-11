from Pedidos.Pedidos_json import (
    ESTADOS_FINALES,
    buscar_pedido_por_id,
    cargar_pedidos,
    guardar_pedidos,
)


def eliminar_pedido():
    print("\n=== CANCELAR PEDIDO ===")
    pedido_id = input("ID del pedido: ").strip()

    if not pedido_id.isdigit():
        print("El ID debe ser numerico.")
        return

    pedidos = cargar_pedidos()
    pedido = buscar_pedido_por_id(pedidos, int(pedido_id))

    if not pedido:
        print("No existe un pedido con ese ID.")
        return

    if pedido.get("estado") in ESTADOS_FINALES:
        print("El pedido ya se encuentra en un estado final.")
        return

    pedido["estado"] = "Cancelado"
    guardar_pedidos(pedidos)
    print("Pedido cancelado correctamente.")
