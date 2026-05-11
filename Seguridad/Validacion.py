from datetime import datetime


def validar_texto_obligatorio(valor, nombre_campo):
    if valor.strip():
        return True

    print(f"{nombre_campo} no puede estar vacio.")
    return False


def validar_entero_positivo(valor, nombre_campo):
    if not valor.isdigit():
        print(f"{nombre_campo} debe ser numerico.")
        return None

    numero = int(valor)
    if numero <= 0:
        print(f"{nombre_campo} debe ser mayor a cero.")
        return None

    return numero


def validar_entero_no_negativo(valor, nombre_campo):
    if not valor.isdigit():
        print(f"{nombre_campo} debe ser numerico.")
        return None

    return int(valor)


def validar_fecha(valor):
    try:
        datetime.strptime(valor, "%d/%m/%Y")
    except ValueError:
        print("La fecha debe tener formato dd/mm/aaaa.")
        return False

    return True


def validar_mail(valor):
    if not valor:
        return True

    if "@" in valor and "." in valor.split("@")[-1]:
        return True

    print("El mail ingresado no tiene un formato valido.")
    return False


def validar_telefono(valor):
    telefono = valor.replace(" ", "").replace("-", "")

    if telefono.isdigit() and len(telefono) >= 6:
        return True

    print("El telefono debe tener al menos 6 digitos.")
    return False


def seleccionar_opcion(valor, opciones, nombre_campo):
    if not valor.isdigit():
        print(f"{nombre_campo} debe ser numerico.")
        return None

    posicion = int(valor)
    if not 1 <= posicion <= len(opciones):
        print(f"{nombre_campo} invalido.")
        return None

    return opciones[posicion - 1]
