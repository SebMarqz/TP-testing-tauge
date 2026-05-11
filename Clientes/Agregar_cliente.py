import json
import uuid
import os

# 1. Buscamos la carpeta actual (Clientes)
DIR_CLIENTES = os.path.dirname(os.path.abspath(__file__))
DIR_RAIZ = os.path.dirname(DIR_CLIENTES)
RUTA_JSON = os.path.join(DIR_RAIZ, 'clientes.json')

def agregar_cliente(nombre, domicilio, telefono, mail):
    id_cliente = str(uuid.uuid4())[:8]
    nuevo_cliente = {
        "id_cliente": id_cliente,
        "nombre": nombre,
        "domicilio": domicilio,
        "telefono": telefono,
        "mail": mail
    }
    
    with open(RUTA_JSON, 'a', encoding='utf-8') as archivo:
        archivo.write(json.dumps(nuevo_cliente, ensure_ascii=False) + '\n')
        
    return nuevo_cliente
