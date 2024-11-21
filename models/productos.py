# Modelo opcional si necesitas validar los datos de empleados
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    
class Producto_post(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int