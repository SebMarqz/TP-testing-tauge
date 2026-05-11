import json
from pathlib import Path


ARCHIVO_STOCK = Path(__file__).resolve().parent / "stock.json"


def cargar_stock():
    if not ARCHIVO_STOCK.exists():
        guardar_stock([])
        return []

    try:
        with ARCHIVO_STOCK.open("r", encoding="utf-8") as archivo:
            stock = json.load(archivo)
    except json.JSONDecodeError:
        return []

    if not isinstance(stock, list):
        return []

    return stock


def guardar_stock(stock):
    with ARCHIVO_STOCK.open("w", encoding="utf-8") as archivo:
        json.dump(stock, archivo, indent=4, ensure_ascii=False)


def obtener_proximo_id(stock):
    if not stock:
        return 1

    ids = [insumo.get("id", 0) for insumo in stock]
    return max(ids) + 1


def buscar_insumo_por_id(stock, insumo_id):
    for insumo in stock:
        if insumo.get("id") == insumo_id:
            return insumo

    return None


def buscar_insumo_por_nombre(stock, nombre):
    for insumo in stock:
        if insumo.get("nombre", "").lower() == nombre.lower():
            return insumo

    return None


def mostrar_insumo(insumo):
    cantidad = insumo.get("cantidad", 0)
    stock_minimo = insumo.get("stock_minimo", 0)
    alerta = " - STOCK BAJO" if cantidad <= stock_minimo else ""

    print(f"ID: {insumo.get('id')}")
    print(f"Nombre: {insumo.get('nombre')}")
    print(f"Cantidad: {cantidad} {insumo.get('unidad')}")
    print(f"Stock minimo: {stock_minimo} {insumo.get('unidad')}{alerta}")
