from Pedidos.Pedidos_json import (
    PAGOS,
    buscar_pedido_por_id,
    cargar_pedidos,
    guardar_pedidos,
)
from Seguridad.Validacion import seleccionar_opcion


def registrar_pago_pedido():
    print("\n=== REGISTRAR PAGO DE PEDIDO ===")
    pedido_id = input("ID del pedido: ").strip()

    if not pedido_id.isdigit():
        print("El ID debe ser numerico.")
        return

    pedidos = cargar_pedidos()
    pedido = buscar_pedido_por_id(pedidos, int(pedido_id))

    if not pedido:
        print("No existe un pedido con ese ID.")
        return

    print("\nEstados de pago:")
    for indice, pago in enumerate(PAGOS, start=1):
        print(f"{indice}. {pago}")

    opcion_pago = input("Seleccione estado de pago: ").strip()
    pago = seleccionar_opcion(opcion_pago, PAGOS, "Estado de pago")
    if not pago:
        return

    pedido["pago"] = pago
    guardar_pedidos(pedidos)
    print("Pago actualizado correctamente.")
