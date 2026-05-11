from Pedidos.Pedidos_json import (
    ESTADOS_FINALES,
    TIPOS_TRABAJO,
    buscar_pedido_por_id,
    cargar_pedidos,
    guardar_pedidos,
)
from Seguridad.Validacion import seleccionar_opcion, validar_fecha


def modificar_pedido():
    print("\n=== MODIFICAR PEDIDO ===")
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
        print("No se puede modificar un pedido entregado o cancelado.")
        return

    cliente = input("Cliente nuevo (enter para mantener): ").strip()
    descripcion = input("Descripcion nueva (enter para mantener): ").strip()
    fecha_estimada = input("Fecha estimada nueva (enter para mantener): ").strip()

    if cliente:
        pedido["cliente"] = cliente
    if descripcion:
        pedido["descripcion"] = descripcion
    if fecha_estimada:
        if not validar_fecha(fecha_estimada):
            return
        pedido["fecha_estimada"] = fecha_estimada

    cambiar_tipo = input("Cambiar tipo de trabajo? (s/n): ").strip().lower()
    if cambiar_tipo == "s":
        for indice, tipo in enumerate(TIPOS_TRABAJO, start=1):
            print(f"{indice}. {tipo}")

        opcion_tipo = input("Seleccione tipo: ").strip()
        tipo_trabajo = seleccionar_opcion(opcion_tipo, TIPOS_TRABAJO, "Tipo de trabajo")
        if not tipo_trabajo:
            return
        pedido["tipo_trabajo"] = tipo_trabajo

    guardar_pedidos(pedidos)
    print("Pedido modificado correctamente.")
