from fastapi import APIRouter, HTTPException, Depends

from models import Pedido
from database import pedidos_db, stock_db
from auth import verificar_usuario

router = APIRouter()

ESTADOS_VALIDOS = {
    "Pendiente": ["En preparación", "Cancelado"],
    "En preparación": ["Listo", "Cancelado"],
    "Listo": ["Entregado", "Cancelado"],
    "Entregado": [],
    "Cancelado": []
}

@router.get("/pedidos", tags=["Pedidos"])
def mostrar_pedidos(
    user = Depends(verificar_usuario)
):

    return pedidos_db

@router.post("/pedidos", tags=["Pedidos"])
def agregar_pedido(
    pedido: Pedido,
    user = Depends(verificar_usuario)
):

    pedido.id = len(pedidos_db) + 1

    for item in pedido.insumos:

        insumo = next(
            (i for i in stock_db if i.id == item.insumo_id),
            None
        )

        if not insumo:

            raise HTTPException(
                status_code=404,
                detail="Insumo no encontrado"
            )

        if insumo.cantidad < item.cantidad:

            raise HTTPException(
                status_code=400,
                detail="Stock insuficiente"
            )

    for item in pedido.insumos:

        insumo = next(
            i for i in stock_db
            if i.id == item.insumo_id
        )

        insumo.cantidad -= item.cantidad

    pedidos_db.append(pedido)

    return pedido

@router.get("/pedidos/buscar", tags=["Pedidos"])
def buscar_pedido(
    cliente_id: int = None,
    estado: str = None,
    user = Depends(verificar_usuario)
):

    resultados = pedidos_db

    if cliente_id:

        resultados = [
            p for p in resultados
            if p.cliente_id == cliente_id
        ]

    if estado:

        resultados = [
            p for p in resultados
            if p.estado == estado
        ]

    return resultados

@router.put("/pedidos/{pedido_id}/estado", tags=["Pedidos"])
def cambiar_estado(
    pedido_id: int,
    nuevo_estado: str,
    user = Depends(verificar_usuario)
):

    for pedido in pedidos_db:

        if pedido.id == pedido_id:

            estado_actual = pedido.estado

            if nuevo_estado not in ESTADOS_VALIDOS[estado_actual]:

                raise HTTPException(
                    status_code=400,
                    detail="Estado inválido"
                )

            pedido.estado = nuevo_estado

            return {
                "mensaje": "Estado actualizado"
            }

    raise HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )

@router.delete("/pedidos/{pedido_id}", tags=["Pedidos"])
def cancelar_pedido(
    pedido_id: int,
    user = Depends(verificar_usuario)
):

    for pedido in pedidos_db:

        if pedido.id == pedido_id:

            pedido.estado = "Cancelado"

            return {
                "mensaje": "Pedido cancelado"
            }

    raise HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )