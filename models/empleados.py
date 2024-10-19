# Modelo opcional si necesitas validar los datos de empleados
from pydantic import BaseModel


class Empleados(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    telefono: str
