from Stock.Stock_json import (
    buscar_insumo_por_id,
    cargar_stock,
    guardar_stock,
    mostrar_insumo,
)
from Seguridad.Validacion import validar_entero_positivo


def quitar_stock():
    print("\n=== QUITAR STOCK ===")
    stock = cargar_stock()

    if not stock:
        print("No hay insumos registrados.")
        return

    for insumo in stock:
        print(f"{insumo.get('id')}. {insumo.get('nombre')} - {insumo.get('cantidad')} {insumo.get('unidad')}")

    insumo_id_texto = input("ID del insumo: ").strip()
    insumo_id = validar_entero_positivo(insumo_id_texto, "ID")
    if insumo_id is None:
        return

    insumo = buscar_insumo_por_id(stock, insumo_id)
    if not insumo:
        print("No existe un insumo con ese ID.")
        return

    cantidad_texto = input("Cantidad a quitar: ").strip()
    cantidad = validar_entero_positivo(cantidad_texto, "Cantidad")
    if cantidad is None:
        return

    if cantidad > insumo.get("cantidad", 0):
        print("No hay stock suficiente para quitar esa cantidad.")
        return

    insumo["cantidad"] = insumo.get("cantidad", 0) - cantidad
    guardar_stock(stock)
    print("Stock descontado correctamente.")
    mostrar_insumo(insumo)
