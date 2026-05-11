from Pedidos.Pedidos_json import (
    ESTADOS,
    buscar_pedido_por_id,
    cargar_pedidos,
    guardar_pedidos,
    puede_cambiar_estado,
)
from Seguridad.Validacion import seleccionar_opcion


def cambiar_estado_pedido():
    print("\n=== CAMBIAR ESTADO DE PEDIDO ===")
    pedido_id = input("ID del pedido: ").strip()

    if not pedido_id.isdigit():
        print("El ID debe ser numerico.")
        return

    pedidos = cargar_pedidos()
    pedido = buscar_pedido_por_id(pedidos, int(pedido_id))

    if not pedido:
        print("No existe un pedido con ese ID.")
        return

    estado_actual = pedido.get("estado")
    print(f"Estado actual: {estado_actual}")
    print("\nEstados disponibles:")
    for indice, estado in enumerate(ESTADOS, start=1):
        print(f"{indice}. {estado}")

    opcion_estado = input("Seleccione nuevo estado: ").strip()
    estado_nuevo = seleccionar_opcion(opcion_estado, ESTADOS, "Estado")
    if not estado_nuevo:
        return

    if not puede_cambiar_estado(estado_actual, estado_nuevo):
        print("Cambio de estado no permitido.")
        return

    pedido["estado"] = estado_nuevo
    guardar_pedidos(pedidos)
    print("Estado actualizado correctamente.")
