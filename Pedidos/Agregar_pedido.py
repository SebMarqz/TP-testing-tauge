from Pedidos.Pedidos_json import (
    PAGOS,
    TIPOS_TRABAJO,
    cargar_pedidos,
    guardar_pedidos,
    obtener_proximo_id,
)
from Seguridad.Validacion import (
    seleccionar_opcion,
    validar_fecha,
    validar_texto_obligatorio,
)


def agregar_pedido():
    print("\n=== AGREGAR PEDIDO ===")
    cliente = input("Cliente: ").strip()
    descripcion = input("Descripcion: ").strip()
    fecha_estimada = input("Fecha estimada (dd/mm/aaaa): ").strip()

    if not validar_texto_obligatorio(cliente, "Cliente"):
        return

    if not validar_texto_obligatorio(descripcion, "Descripcion"):
        return

    if not validar_texto_obligatorio(fecha_estimada, "Fecha estimada"):
        return

    if not validar_fecha(fecha_estimada):
        return

    print("\nTipos de trabajo:")
    for indice, tipo in enumerate(TIPOS_TRABAJO, start=1):
        print(f"{indice}. {tipo}")

    opcion_tipo = input("Seleccione tipo: ").strip()
    tipo_trabajo = seleccionar_opcion(opcion_tipo, TIPOS_TRABAJO, "Tipo de trabajo")
    if not tipo_trabajo:
        return

    pago = input("Pago (Pendiente/Pagado): ").strip().capitalize()
    if pago not in PAGOS:
        pago = "Pendiente"

    pedidos = cargar_pedidos()
    pedido = {
        "id": obtener_proximo_id(pedidos),
        "cliente": cliente,
        "descripcion": descripcion,
        "fecha_estimada": fecha_estimada,
        "tipo_trabajo": tipo_trabajo,
        "estado": "Pendiente",
        "pago": pago,
    }

    pedidos.append(pedido)
    guardar_pedidos(pedidos)
    print(f"Pedido registrado correctamente. ID asignado: {pedido['id']}")
