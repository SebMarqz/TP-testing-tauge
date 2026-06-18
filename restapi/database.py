import json
import os
from fastapi.encoders import jsonable_encoder
from models import Cliente, Pedido, Insumo

# Definimos los nombres de los archivos físicos
CLIENTES_FILE = "clientes.json"
PEDIDOS_FILE = "pedidos.json"
STOCK_FILE = "stock.json"
USUARIOS_FILE = "usuarios.json"

def cargar_datos(archivo, por_defecto):
    """Carga los datos desde el archivo JSON si existe, sino devuelve el valor por defecto."""
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return por_defecto

def guardar_datos(archivo, datos):
    """Guarda la estructura de datos en formato JSON."""
    with open(archivo, "w", encoding="utf-8") as f:
        # jsonable_encoder convierte los modelos Pydantic a diccionarios compatibles con JSON
        json.dump(jsonable_encoder(datos), f, indent=4)

# Cargar datos a la memoria e instanciarlos como modelos de Pydantic
clientes_db = [Cliente(**c) for c in cargar_datos(CLIENTES_FILE, [])]
pedidos_db = [Pedido(**p) for p in cargar_datos(PEDIDOS_FILE, [])]
stock_db = [Insumo(**i) for i in cargar_datos(STOCK_FILE, [])]

usuarios_por_defecto = {
    "admin": {
        "username": "admin",
        "password": "123",
        "rol": "Administrador"
    }
}
usuarios_db = cargar_datos(USUARIOS_FILE, usuarios_por_defecto)

# Funciones de guardado específicas que llamaremos desde los routers
def guardar_clientes():
    guardar_datos(CLIENTES_FILE, clientes_db)

def guardar_pedidos():
    guardar_datos(PEDIDOS_FILE, pedidos_db)

def guardar_stock():
    guardar_datos(STOCK_FILE, stock_db)

def guardar_usuarios():
    guardar_datos(USUARIOS_FILE, usuarios_db)