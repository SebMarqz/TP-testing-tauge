from fastapi import FastAPI

from Clientes.clientes import router as clientes_router
from Pedidos.pedidos import router as pedidos_router
from Stock.stock import router as stock_router
from Seguridad.seguridad import router as seguridad_router
from Usuario.usuarios import router as usuarios_router

app = FastAPI(
    title="Tauge API",
    version="1.0.0",
    description="Sistema Web Service API"
)

app.include_router(seguridad_router)

app.include_router(clientes_router)

app.include_router(stock_router)

app.include_router(pedidos_router)

app.include_router(usuarios_router)
