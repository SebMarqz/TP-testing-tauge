import requests
from API.api_client import BASE_URL, headers_auth


def agregar_cliente():
    print('\n=== AGREGAR CLIENTE ===')
    cliente={
        'id': int(input('ID: ')),
        'nombre': input('Nombre: ').strip(),
        'telefono': input('Telefono: ').strip(),
        'email': input('Email: ').strip()
    }
    response=requests.post(f'{BASE_URL}/clientes',json=cliente,headers=headers_auth())
    print(response.json() if response.headers.get('content-type','').startswith('application/json') else response.text)
