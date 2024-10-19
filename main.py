from core.connection import *
from models.productos import Producto
from models.user import User
from models.empleados import *


# Ruta POST para iniciar sesión
@app.post("/login_users")
async def login(user: User):
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Consulta SQL para verificar si el usuario y la contraseña coinciden
            sql = "SELECT email, password FROM login_users WHERE email = %s"
            cursor.execute(sql, (user.email,))
            result = cursor.fetchone()  # Obtener un solo resultado

            # Verificar si el usuario existe y la contraseña es correcta
            if result is None:
                raise HTTPException(status_code=400, detail="User not found")
            
            if result['password'] != user.password:
                raise HTTPException(status_code=400, detail="Invalid credentials")

            # Si todo es correcto, devolver el mensaje de éxito
            return {"message": "Login successful"}

    except Exception as e:
        print(f"Error: {e}")  # Imprimir el error en la consola para depurar
        raise HTTPException(status_code=500, detail="Internal server error")

    finally:
        connection.close()  # Cerrar la conexión

# Ruta GET para obtener los datos de todos los empleados
@app.get("/empleados", response_model=List[dict])
async def empleados():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Consulta SQL para obtener todos los empleados
            sql = "SELECT id, nombre, apellido, email, telefono FROM empleados"
            cursor.execute(sql)
            result = cursor.fetchall()  # Obtener todos los resultados de la consulta

            # Devolver los resultados como JSON (FastAPI lo hace automáticamente)
            return result

    except Exception as e:
        print(f"Error: {e}")  # Imprimir el error en la consola para depurar
        raise HTTPException(status_code=500, detail="Internal server error")

    finally:
        connection.close()  # Cerrar la conexión


# Ruta GET para obtener los datos de todos los productos
@app.get("/productos", response_model=List[Producto])
async def obtener_productos():
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Consulta SQL para obtener todos los productos
            sql = "SELECT id, nombre, descripcion, precio, cantidad FROM productos"
            cursor.execute(sql)
            result = cursor.fetchall()  # Obtener todos los resultados de la consulta

            # Devolver los resultados como JSON (FastAPI lo hace automáticamente)
            return result

    except Exception as e:
        print(f"Error: {e}")  # Imprimir el error en la consola para depurar
        raise HTTPException(status_code=500, detail="Internal server error")

    finally:
        connection.close()  # Cerrar la conexión