from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LoginModel(BaseModel):
    username: str
    password: str

class Cliente(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: Optional[str] = None

class Usuario(BaseModel):
    username: str
    password: str
    rol: str

class Insumo(BaseModel):
    id: int
    nombre: str
    cantidad: int
    unidad: str
    stock_minimo: int = 10

class PedidoItem(BaseModel):
    insumo_id: int
    cantidad: int

class Pedido(BaseModel):

    id: int

    cliente_id: int

    descripcion: str

    tipo_trabajo: str

    fecha_estimada: str

    estado: str = "Pendiente"

    estado_pago: str = "Pendiente"

    insumos: List[PedidoItem] = []

    fecha_creacion: str = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
