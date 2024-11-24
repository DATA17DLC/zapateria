# Modelo opcional si necesitas validar los datos de empleados
from typing import Optional, List
from unittest.mock import Base
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql


class Empleados(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    telefono: str

class Empleados_post(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str
    
