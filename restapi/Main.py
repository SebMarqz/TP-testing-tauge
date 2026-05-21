import logging
from fastapi import FastAPI

from Clientes.clientes import router as clientes_router
from Pedidos.pedidos import router as pedidos_router
from Stock.stock import router as stock_router
from Seguridad.seguridad import router as seguridad_router
from Usuario.usuarios import router as usuarios_router

# Configuración global de Logs
logging.basicConfig(
    level=logging.INFO, # Nivel mínimo de eventos que registrará (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        # El mode="w" sobrescribe el archivo en cada inicio del servidor
        logging.FileHandler("api.log", mode="w", encoding="utf-8"), # Guarda en un archivo permanente
        logging.StreamHandler()                            # Muestra en la consola de VS Code
    ]
)
logging.getLogger("watchfiles.main").setLevel(logging.WARNING) # Evita logs de recarga automática de FastAPI

# Creamos un logger específico para el archivo principal
logger = logging.getLogger("Main")

app = FastAPI(
    title="Tauge API",
    version="1.0.0",
    description="Sistema Web Service API"
)

# Log de inicio del sistema
logger.info("Iniciando el Web Service Tauge API y cargando rutas...")

app.include_router(seguridad_router)
app.include_router(clientes_router)
app.include_router(stock_router)
app.include_router(pedidos_router)
app.include_router(usuarios_router)

logger.info("Aplicación lista para recibir peticiones.")