import json
import os

# Configuramos la ruta dinámica absoluta
DIR_CLIENTES = os.path.dirname(os.path.abspath(__file__))
DIR_RAIZ = os.path.dirname(DIR_CLIENTES)
RUTA_JSON = os.path.join(DIR_RAIZ, 'clientes.json')

def eliminar_cliente(id_cliente):
    """Elimina un cliente del JSON mediante su ID."""
    if not os.path.exists(RUTA_JSON):
        return False

    ruta_temp = os.path.join(DIR_RAIZ, 'clientes_temp.json')
    eliminado = False

    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo_lectura, \
         open(ruta_temp, 'w', encoding='utf-8') as archivo_escritura:
         
        for linea in archivo_lectura:
            if linea.strip():
                cliente = json.loads(linea.strip())
                
                # Si es el que queremos eliminar, NO lo copiamos
                if cliente["id_cliente"] == id_cliente:
                    eliminado = True
                    continue 
                
                # Si no es, lo copiamos al archivo temporal
                archivo_escritura.write(linea)

    # Reemplazamos el archivo viejo por el nuevo
    os.replace(ruta_temp, RUTA_JSON)
    return eliminado
