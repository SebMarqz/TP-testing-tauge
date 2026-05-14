import requests

BASE_URL='http://127.0.0.1:8000'
token=None


def headers_auth():
    return {'Authorization': f'Bearer {token}'} if token else {}


def login(username,password):
    global token
    r=requests.post(f'{BASE_URL}/login',json={'username':username,'password':password})
    if r.status_code==200:
        data=r.json(); token=data.get('token'); return data
    return None
