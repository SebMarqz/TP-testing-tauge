import logging
from fastapi import APIRouter, HTTPException, Depends
from models import Pedido
from database import pedidos_db, stock_db, guardar_pedidos, guardar_stock
from auth import verificar_usuario

router = APIRouter()
logger = logging.getLogger("Pedidos")

@router.post("/pedidos", tags=["Pedidos"])
def agregar_pedido(pedido: Pedido, user = Depends(verificar_usuario)):
    logger.info(f"Usuario '{user['username']}' intentando crear un nuevo pedido.")

    pedido.id = len(pedidos_db) + 1

    # Validación de stock
    for item in pedido.insumos:
        insumo = next((i for i in stock_db if i.id == item.insumo_id), None)
        if not insumo:
            logger.error(f"Error al crear pedido: Insumo ID {item.insumo_id} no existe.")
            raise HTTPException(status_code=404, detail="Insumo no encontrado")
        if insumo.cantidad < item.cantidad:
            logger.warning(f"Stock insuficiente para Insumo '{insumo.nombre}' (ID {insumo.id}). Requerido: {item.cantidad}, Disponible: {insumo.cantidad}")
            raise HTTPException(status_code=400, detail="Stock insuficiente")

    # Descontar del stock
    for item in pedido.insumos:
        insumo = next((i for i in stock_db if i.id == item.insumo_id), None)
        insumo.cantidad -= item.cantidad

    pedidos_db.append(pedido)
    guardar_pedidos()
    guardar_stock()
    
    logger.info(f"Pedido ID {pedido.id} creado con éxito por '{user['username']}'. Stock actualizado.")
    return pedido

@router.delete("/pedidos/{pedido_id}", tags=["Pedidos"])
def cancelar_pedido(pedido_id: int, user = Depends(verificar_usuario)):
    for pedido in pedidos_db:
        if pedido.id == pedido_id:
            pedido.estado = "Cancelado"
            guardar_pedidos()
            logger.info(f"Pedido ID {pedido_id} fue CANCELADO por el usuario '{user['username']}'.")
            return {"mensaje": "Pedido cancelado"}
            
    logger.error(f"Intento fallido de cancelar pedido: ID {pedido_id} no existe.")
    raise HTTPException(status_code=404, detail="Pedido no encontrado")