from typing import List
from fastapi import FastAPI, HTTPException
import pymysql
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración del CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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