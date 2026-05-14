import requests
from API.api_client import BASE_URL, headers_auth


def eliminar_cliente():
    cliente_id=input('ID cliente: ').strip()
    response=requests.delete(f'{BASE_URL}/clientes/{cliente_id}',headers=headers_auth())
    print(response.json() if response.headers.get('content-type','').startswith('application/json') else response.text)
