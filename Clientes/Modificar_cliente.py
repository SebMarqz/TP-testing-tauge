import json
import os

# Configuramos la ruta dinámica absoluta
DIR_CLIENTES = os.path.dirname(os.path.abspath(__file__))
DIR_RAIZ = os.path.dirname(DIR_CLIENTES)
RUTA_JSON = os.path.join(DIR_RAIZ, 'clientes.json')

def modificar_cliente(id_cliente, datos_actualizados):
    """Modifica los datos de un cliente existente y actualiza el archivo."""
    if not os.path.exists(RUTA_JSON):
        return None

    ruta_temp = os.path.join(DIR_RAIZ, 'clientes_temp.json')
    cliente_modificado = None

    with open(RUTA_JSON, 'r', encoding='utf-8') as archivo_lectura, \
         open(ruta_temp, 'w', encoding='utf-8') as archivo_escritura:
        
        for linea in archivo_lectura:
            if linea.strip():
                cliente = json.loads(linea.strip())
                
                # Si es el cliente que queremos modificar
                if cliente["id_cliente"] == id_cliente:
                    # Actualizamos los datos
                    for key, value in datos_actualizados.items():
                        if key in cliente:
                            cliente[key] = value
                    cliente_modificado = cliente
                    
                    # Escribimos el cliente ya modificado
                    archivo_escritura.write(json.dumps(cliente_modificado, ensure_ascii=False) + '\n')
                else:
                    # Si no es, lo pasamos al archivo temporal tal cual estaba
                    archivo_escritura.write(linea)
                    
    # Reemplazamos el archivo viejo por el nuevo
    os.replace(ruta_temp, RUTA_JSON)
    return cliente_modificado
