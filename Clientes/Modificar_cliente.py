import requests
from API.api_client import BASE_URL, headers_auth


def modificar_cliente():
    cliente_id=input('ID cliente: ').strip()
    cliente={
        'id': int(cliente_id),
        'nombre': input('Nombre: ').strip(),
        'telefono': input('Telefono: ').strip(),
        'email': input('Email: ').strip()
    }
    response=requests.put(f'{BASE_URL}/clientes/{cliente_id}',json=cliente,headers=headers_auth())
    print(response.json() if response.headers.get('content-type','').startswith('application/json') else response.text)
