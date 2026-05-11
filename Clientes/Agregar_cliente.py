from Clientes.Clientes_json import cargar_clientes, guardar_clientes, obtener_proximo_id
from Seguridad.Validacion import (
    validar_mail,
    validar_telefono,
    validar_texto_obligatorio,
)


def agregar_cliente():
    print("\n=== AGREGAR CLIENTE ===")
    nombre = input("Nombre: ").strip()
    domicilio = input("Domicilio: ").strip()
    telefono = input("Telefono: ").strip()
    mail = input("Mail: ").strip()

    if not validar_texto_obligatorio(nombre, "Nombre"):
        return

    if not validar_telefono(telefono):
        return

    if not validar_mail(mail):
        return

    clientes = cargar_clientes()
    cliente = {
        "id": obtener_proximo_id(clientes),
        "nombre": nombre,
        "domicilio": domicilio,
        "telefono": telefono,
        "mail": mail,
    }

    clientes.append(cliente)
    guardar_clientes(clientes)
    print(f"Cliente agregado correctamente. ID asignado: {cliente['id']}")
