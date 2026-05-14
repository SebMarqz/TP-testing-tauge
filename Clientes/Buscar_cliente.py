import requests
from API.api_client import BASE_URL, headers_auth


def buscar_cliente():
    cliente_id=input('ID cliente: ').strip()
    response=requests.get(f'{BASE_URL}/clientes/{cliente_id}',headers=headers_auth())
    print(response.json() if response.status_code==200 else response.text)
