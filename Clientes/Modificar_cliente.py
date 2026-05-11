from Clientes.Clientes_json import (
    buscar_cliente_por_id,
    cargar_clientes,
    guardar_clientes,
)
from Seguridad.Validacion import validar_mail, validar_telefono


def modificar_cliente():
    print("\n=== MODIFICAR CLIENTE ===")
    cliente_id = input("ID del cliente: ").strip()

    if not cliente_id.isdigit():
        print("El ID debe ser numerico.")
        return

    clientes = cargar_clientes()
    cliente = buscar_cliente_por_id(clientes, int(cliente_id))

    if not cliente:
        print("No existe un cliente con ese ID.")
        return

    nombre = input("Nombre nuevo (enter para mantener): ").strip()
    domicilio = input("Domicilio nuevo (enter para mantener): ").strip()
    telefono = input("Telefono nuevo (enter para mantener): ").strip()
    mail = input("Mail nuevo (enter para mantener): ").strip()

    if nombre:
        cliente["nombre"] = nombre
    if domicilio:
        cliente["domicilio"] = domicilio
    if telefono:
        if not validar_telefono(telefono):
            return
        cliente["telefono"] = telefono
    if mail:
        if not validar_mail(mail):
            return
        cliente["mail"] = mail

    guardar_clientes(clientes)
    print("Cliente modificado correctamente.")
