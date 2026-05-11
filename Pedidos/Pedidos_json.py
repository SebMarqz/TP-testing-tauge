import json
from pathlib import Path


ARCHIVO_PEDIDOS = Path(__file__).resolve().parent / "pedidos.json"
ESTADOS = ["Pendiente", "En preparacion", "Listo", "Entregado", "Cancelado"]
PAGOS = ["Pendiente", "Pagado"]
TIPOS_TRABAJO = [
    "Impresion simple",
    "Diseno e impresion",
    "Terminaciones",
    "Grafica especial",
    "Otros",
]
ESTADOS_FINALES = ["Entregado", "Cancelado"]
TRANSICIONES_VALIDAS = {
    "Pendiente": ["En preparacion", "Cancelado"],
    "En preparacion": ["Listo", "Cancelado"],
    "Listo": ["Entregado", "Cancelado"],
    "Entregado": [],
    "Cancelado": [],
}


def cargar_pedidos():
    if not ARCHIVO_PEDIDOS.exists():
        guardar_pedidos([])
        return []

    try:
        with ARCHIVO_PEDIDOS.open("r", encoding="utf-8") as archivo:
            pedidos = json.load(archivo)
    except json.JSONDecodeError:
        return []

    if not isinstance(pedidos, list):
        return []

    return pedidos


def guardar_pedidos(pedidos):
    with ARCHIVO_PEDIDOS.open("w", encoding="utf-8") as archivo:
        json.dump(pedidos, archivo, indent=4, ensure_ascii=False)


def obtener_proximo_id(pedidos):
    if not pedidos:
        return 1

    ids = [pedido.get("id", 0) for pedido in pedidos]
    return max(ids) + 1


def buscar_pedido_por_id(pedidos, pedido_id):
    for pedido in pedidos:
        if pedido.get("id") == pedido_id:
            return pedido

    return None


def puede_cambiar_estado(estado_actual, estado_nuevo):
    return estado_nuevo in TRANSICIONES_VALIDAS.get(estado_actual, [])


def mostrar_resumen_pedido(pedido):
    print(f"ID: {pedido.get('id')}")
    print(f"Cliente: {pedido.get('cliente')}")
    print(f"Tipo: {pedido.get('tipo_trabajo')}")
    print(f"Descripcion: {pedido.get('descripcion')}")
    print(f"Fecha estimada: {pedido.get('fecha_estimada')}")
    print(f"Estado: {pedido.get('estado')}")
    print(f"Pago: {pedido.get('pago')}")
