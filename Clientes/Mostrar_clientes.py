import requests
from API.api_client import BASE_URL, headers_auth


def mostrar_clientes():
    response=requests.get(f'{BASE_URL}/clientes',headers=headers_auth())
    if response.status_code!=200:
        print('Error al obtener clientes')
        print(response.text)
        return
    clientes=response.json()
    print('\n=== CLIENTES ===')
    for c in clientes:
        print(c)
