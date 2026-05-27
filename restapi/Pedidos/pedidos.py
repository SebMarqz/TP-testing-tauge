import logging
from fastapi import APIRouter, HTTPException, Depends
from models import Pedido
from database import pedidos_db, stock_db, guardar_pedidos, guardar_stock
from auth import verificar_usuario

router = APIRouter()
logger = logging.getLogger("Pedidos")

ESTADOS_VALIDOS = {
    "Pendiente": ["En preparacion", "Cancelado"],
    "En preparacion": ["Listo", "Cancelado"],
    "Listo": ["Entregado", "Cancelado"],
    "Entregado": [],
    "Cancelado": []
}

@router.get("/pedidos", tags=["Pedidos"])
def mostrar_pedidos(cliente_id: int = None, estado: str = None, user = Depends(verificar_usuario)):
    # Iniciamos con todos los pedidos en memoria
    resultados = pedidos_db
    
    # Aplicamos filtros dinámicamente si los parámetros vienen en la URL
    if cliente_id:
        resultados = [p for p in resultados if p.cliente_id == cliente_id]
    if estado:
        resultados = [p for p in resultados if p.estado == estado]
        
    return resultados

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

@router.put("/pedidos/{pedido_id}", tags=["Pedidos"])
def modificar_pedido(pedido_id: int, nuevo_pedido: Pedido, user = Depends(verificar_usuario)):
    logger.info(f"Usuario '{user['username']}' intentando modificar el pedido ID {pedido_id}.")
    
    for i, pedido in enumerate(pedidos_db):
        if pedido.id == pedido_id:
            
            # Si ya está Entregado o Cancelado, bloqueamos la edición
            if pedido.estado in ["Entregado", "Cancelado"]:
                logger.warning(f"Intento de modificar un pedido bloqueado. ID {pedido_id} está en estado '{pedido.estado}'.")
                raise HTTPException(
                    status_code=400,
                    detail=f"No se puede modificar un pedido que ya se encuentra en estado '{pedido.estado}'."
                )
            
            # Si pasa el filtro, se edita normalmente
            nuevo_pedido.id = pedido_id
            nuevo_pedido.fecha_creacion = pedido.fecha_creacion
            
            pedidos_db[i] = nuevo_pedido
            guardar_pedidos()
            
            logger.info(f"Pedido ID {pedido_id} modificado con éxito por '{user['username']}'.")
            return {"mensaje": "Pedido actualizado", "pedido": nuevo_pedido}
            
    logger.error(f"Intento fallido de modificar pedido: ID {pedido_id} no existe.")
    raise HTTPException(status_code=404, detail="Pedido no encontrado")

@router.put("/pedidos/{pedido_id}/estado", tags=["Pedidos"])
def cambiar_estado(pedido_id: int, nuevo_estado: str, user = Depends(verificar_usuario)):
    for pedido in pedidos_db:
        if pedido.id == pedido_id:
            estado_actual = pedido.estado

            if nuevo_estado not in ESTADOS_VALIDOS[estado_actual]:
                logger.warning(f"Usuario '{user['username']}' intentó un cambio de estado inválido para el Pedido ID {pedido_id}: de '{estado_actual}' a '{nuevo_estado}'")
                raise HTTPException(
                    status_code=400,
                    detail=f"Estado inválido. No se puede pasar de '{estado_actual}' a '{nuevo_estado}'."
                )

            pedido.estado = nuevo_estado
            guardar_pedidos()
            logger.info(f"Pedido ID {pedido_id} cambió de estado a '{nuevo_estado}' por usuario '{user['username']}'.")
            return {"mensaje": "Estado actualizado", "nuevo_estado": pedido.estado}

    raise HTTPException(status_code=404, detail="Pedido no encontrado")

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