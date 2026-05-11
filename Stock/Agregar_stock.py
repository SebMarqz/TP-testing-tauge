from Stock.Stock_json import (
    buscar_insumo_por_nombre,
    cargar_stock,
    guardar_stock,
    obtener_proximo_id,
)
from Seguridad.Validacion import (
    validar_entero_no_negativo,
    validar_entero_positivo,
    validar_texto_obligatorio,
)


def agregar_stock():
    print("\n=== AGREGAR STOCK ===")
    nombre = input("Nombre del insumo: ").strip()

    if not validar_texto_obligatorio(nombre, "Nombre del insumo"):
        return

    cantidad_texto = input("Cantidad a agregar: ").strip()
    cantidad = validar_entero_positivo(cantidad_texto, "Cantidad")
    if cantidad is None:
        return

    stock = cargar_stock()
    insumo = buscar_insumo_por_nombre(stock, nombre)

    if insumo:
        insumo["cantidad"] = insumo.get("cantidad", 0) + cantidad
        guardar_stock(stock)
        print("Stock actualizado correctamente.")
        return

    unidad = input("Unidad (ej: hojas, unidades, metros): ").strip()
    if not unidad:
        unidad = "unidades"

    minimo_texto = input("Stock minimo para alerta: ").strip()
    if minimo_texto:
        stock_minimo = validar_entero_no_negativo(minimo_texto, "Stock minimo")
        if stock_minimo is None:
            return
    else:
        stock_minimo = 0

    stock.append(
        {
            "id": obtener_proximo_id(stock),
            "nombre": nombre,
            "cantidad": cantidad,
            "unidad": unidad,
            "stock_minimo": stock_minimo,
        }
    )
    guardar_stock(stock)
    print("Insumo agregado correctamente.")
