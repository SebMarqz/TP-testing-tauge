from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class LoginModel(BaseModel):
    username: str
    password: str

class Cliente(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1)  # Obliga a tener mínimo 1 carácter
    telefono: str = Field(..., min_length=1)
    email: Optional[str] = None

class Usuario(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)
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
    id: int = 0  # Permite omitirlo en el POST sin fallar por Pydantic
    cliente_id: int
    descripcion: str = Field(..., min_length=1)
    tipo_trabajo: str = Field(..., min_length=1)
    fecha_estimada: str = Field(..., min_length=1)
    estado: str = "Pendiente"
    estado_pago: str = "Pendiente"
    insumos: List[PedidoItem] = []
    fecha_creacion: str = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )