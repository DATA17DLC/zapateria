from typing import List
from fastapi import FastAPI, HTTPException
import pymysql
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Agregar middleware de CORS
origins = [
    "*",  # Para permitir todas las solicitudes (menos recomendado para producción)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir los orígenes definidos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)



# Función para configurar la conexión a MySQL
def connection_mysql():
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="zapateria",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion

