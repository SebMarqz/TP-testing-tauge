import json
import os

# Hacemos EXACTAMENTE lo mismo con la ruta acá
DIR_CLIENTES = os.path.dirname(os.path.abspath(__file__))
DIR_RAIZ = os.path.dirname(DIR_CLIENTES)
RUTA_JSON = os.path.join(DIR_RAIZ, 'clientes.json')

def mostrar_todos_los_clientes():
    """Lee y muestra los clientes sin cargar todo el archivo en memoria."""
    if not os.path.exists(RUTA_JSON):
        print("No hay clientes registrados actualmente.")
        return

    print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
    
    # Leemos línea por línea
    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if linea.strip(): 
                cliente = json.loads(linea.strip())
                print(f"ID: {cliente['id_cliente']} | Nombre: {cliente['nombre']} | Tel: {cliente['telefono']}")
                
    print("-------------------------------------\n")
