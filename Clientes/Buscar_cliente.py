import json
import os

# Configuramos la ruta dinámica absoluta
DIR_CLIENTES = os.path.dirname(os.path.abspath(__file__))
DIR_RAIZ = os.path.dirname(DIR_CLIENTES)
RUTA_JSON = os.path.join(DIR_RAIZ, 'clientes.json')

def buscar_cliente_por_id(id_cliente):
    """Busca un cliente específico por su ID."""
    if not os.path.exists(RUTA_JSON):
        return None
        
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if linea.strip():
                cliente = json.loads(linea.strip())
                if cliente["id_cliente"] == id_cliente:
                    return cliente # Corta la ejecución apenas lo encuentra
    return None

def buscar_cliente_por_nombre(nombre_buscar):
    """Busca clientes que coincidan parcialmente con el nombre ingresado."""
    resultados = []
    if not os.path.exists(RUTA_JSON):
        return resultados
        
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if linea.strip():
                cliente = json.loads(linea.strip())
                if nombre_buscar.lower() in cliente["nombre"].lower():
                    resultados.append(cliente)
    return resultados
