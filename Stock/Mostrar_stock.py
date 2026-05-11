from Stock.Stock_json import cargar_stock, mostrar_insumo


def mostrar_stock():
    print("\n=== STOCK DISPONIBLE ===")
    stock = cargar_stock()

    if not stock:
        print("No hay insumos registrados.")
        return

    for insumo in stock:
        mostrar_insumo(insumo)
        print("-" * 30)
