import json
from pathlib import Path


ARCHIVO_CLIENTES = Path(__file__).resolve().parent / "clientes.json"


def cargar_clientes():
    if not ARCHIVO_CLIENTES.exists():
        guardar_clientes([])
        return []

    try:
        with ARCHIVO_CLIENTES.open("r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
    except json.JSONDecodeError:
        return []

    if not isinstance(clientes, list):
        return []

    return clientes


def guardar_clientes(clientes):
    with ARCHIVO_CLIENTES.open("w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)


def obtener_proximo_id(clientes):
    if not clientes:
        return 1

    ids = [cliente.get("id", 0) for cliente in clientes]
    return max(ids) + 1


def buscar_cliente_por_id(clientes, cliente_id):
    for cliente in clientes:
        if cliente.get("id") == cliente_id:
            return cliente

    return None


def mostrar_cliente(cliente):
    print(f"ID: {cliente.get('id')}")
    print(f"Nombre: {cliente.get('nombre')}")
    print(f"Domicilio: {cliente.get('domicilio')}")
    print(f"Telefono: {cliente.get('telefono')}")
    print(f"Mail: {cliente.get('mail')}")
