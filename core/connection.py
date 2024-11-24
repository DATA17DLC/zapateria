from typing import List
from fastapi import FastAPI, HTTPException, Depends
import pymysql
from pydantic import BaseModel


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

