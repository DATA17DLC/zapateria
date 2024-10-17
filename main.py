from fastapi import FastAPI, HTTPException
import pymysql
from typing import List
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
    conexion = pymysql.connect(host="localhost",  # Corregido de 'hots' a 'host'
                               user="root",
                               password="1234",
                               database="zapateria",
                               cursorclass=pymysql.cursors.DictCursor)
    return conexion

# Definir un modelo para los datos del usuario
class User(BaseModel):
    email: str
    password: str

# Definir la ruta para iniciar sesión
@app.post("/login_users")
async def login(user: User):
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Consulta para obtener el usuario
            sql = "SELECT email, password FROM login_users WHERE email = %s"
            cursor.execute(sql, (user.email,))
            result = cursor.fetchone()  # Obtener solo un resultado

            # Verificar las credenciales
            if result is None or result['password'] != user.password:
                raise HTTPException(status_code=400, detail="Invalid credentials")

            # Devolver mensaje de éxito
            return {"message": "Login successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        connection.close()  # Cerrar la conexión
