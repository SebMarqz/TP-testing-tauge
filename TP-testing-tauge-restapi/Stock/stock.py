from fastapi import APIRouter, HTTPException, Depends

from models import Insumo
from database import stock_db
from auth import verificar_usuario

router = APIRouter()

@router.get("/stock", tags=["Stock"])
def mostrar_stock(
    user = Depends(verificar_usuario)
):

    alertas = []

    for insumo in stock_db:

        if insumo.cantidad <= insumo.stock_minimo:

            alertas.append(
                f"Stock bajo: {insumo.nombre}"
            )

    return {
        "stock": stock_db,
        "alertas": alertas
    }

@router.post("/stock", tags=["Stock"])
def agregar_stock(
    insumo: Insumo,
    user = Depends(verificar_usuario)
):

    stock_db.append(insumo)

    return insumo

@router.put("/stock/{insumo_id}", tags=["Stock"])
def quitar_stock(
    insumo_id: int,
    cantidad: int,
    user = Depends(verificar_usuario)
):

    for insumo in stock_db:

        if insumo.id == insumo_id:

            if insumo.cantidad < cantidad:

                raise HTTPException(
                    status_code=400,
                    detail="Stock insuficiente"
                )

            insumo.cantidad -= cantidad

            return {
                "mensaje": "Stock actualizado",
                "insumo": insumo
            }

    raise HTTPException(
        status_code=404,
        detail="Insumo no encontrado"
    )