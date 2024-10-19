from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    cantidad: int