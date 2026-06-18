from fastapi import APIRouter, HTTPException, Depends
from typing import List

from models import Cliente
from database import clientes_db, guardar_clientes
from auth import verificar_usuario

router = APIRouter()

@router.get("/clientes", response_model=List[Cliente], tags=["Clientes"])
def mostrar_clientes(user = Depends(verificar_usuario)):
    return clientes_db

@router.post("/clientes", response_model=Cliente, tags=["Clientes"])
def agregar_cliente(cliente: Cliente, user = Depends(verificar_usuario)):
    clientes_db.append(cliente)
    guardar_clientes()
    return cliente

@router.get("/clientes/{cliente_id}", tags=["Clientes"])
def buscar_cliente(cliente_id: int, user = Depends(verificar_usuario)):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.put("/clientes/{cliente_id}", tags=["Clientes"])
def modificar_cliente(cliente_id: int, nuevo_cliente: Cliente, user = Depends(verificar_usuario)):
    for i, cliente in enumerate(clientes_db):
        if cliente.id == cliente_id:
            clientes_db[i] = nuevo_cliente
            guardar_clientes()
            return {"mensaje": "Cliente actualizado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.delete("/clientes/{cliente_id}", tags=["Clientes"])
def eliminar_cliente(cliente_id: int, user = Depends(verificar_usuario)):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            clientes_db.remove(cliente)
            guardar_clientes()
            return {"mensaje": "Cliente eliminado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")