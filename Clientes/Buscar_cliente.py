from Clientes.Clientes_json import cargar_clientes, mostrar_cliente


def buscar_cliente():
    print("\n=== BUSCAR CLIENTE ===")
    print("1. Por ID")
    print("2. Por nombre")
    print("3. Por telefono")
    opcion = input("Ingrese opcion: ").strip()

    clientes = cargar_clientes()
    resultados = []

    if opcion == "1":
        cliente_id = input("ID del cliente: ").strip()
        if not cliente_id.isdigit():
            print("El ID debe ser numerico.")
            return
        resultados = [cliente for cliente in clientes if cliente.get("id") == int(cliente_id)]
    elif opcion == "2":
        nombre = input("Nombre: ").strip().lower()
        resultados = [
            cliente for cliente in clientes if nombre in cliente.get("nombre", "").lower()
        ]
    elif opcion == "3":
        telefono = input("Telefono: ").strip()
        resultados = [
            cliente for cliente in clientes if telefono in cliente.get("telefono", "")
        ]
    else:
        print("Opcion invalida.")
        return

    if not resultados:
        print("No se encontraron clientes.")
        return

    for cliente in resultados:
        mostrar_cliente(cliente)
        print("-" * 30)
