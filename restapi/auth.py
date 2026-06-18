from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from database import usuarios_db

security = HTTPBearer()

def verificar_usuario(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    if not token.startswith("fake-token-"):

        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    username = token.replace("fake-token-", "")

    if username not in usuarios_db:

        raise HTTPException(
            status_code=401,
            detail="Usuario no autorizado"
        )

    return usuarios_db[username]