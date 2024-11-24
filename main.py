from core.connection import *
from models.productos import *
from models.user import User
from models.empleados import *

from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por los dominios permitidos en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

"################################### LOGIN #######################################"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class UserLogin(BaseModel):
    username : str
    password : str

users = {
    "admin": {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "1234"
    }
}

# Simula la generación de un token
def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, key="secret", algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        data = jwt.decode(token, key="secret", algorithms="HS256") 
        return data
    except jwt.JWTerror as e:
        raise HTTPException(status_code=401, detail="invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Ruta de inicio de sesión
@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # Busca al usuario en el diccionario
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Genera el token
    token = encode_token({"username": user["username"], "email": user["email"]})

    return {"access_token": token, "token_type": "bearer"}

# Ruta de inicio de sesión
@app.post("/login_json")
async def login(form_data:UserLogin):
    # Busca al usuario en el diccionario
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=404, detail="incorret username or password")

    # Genera el token
    token = encode_token({"username": user["username"], "email": user["email"]})

    return {"access_token": token, "token_type": "bearer"}

@app.get("/users/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user

@app.get("/users", dependencies=[Depends(decode_token)])
def user_list():
    return users
"###############################################################################################"
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

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

"################################### CRUD PARA EMPLEADOS #######################################"

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
        
# metodo para agregar empleados        
@app.post("/empleados")
async def crear_empleado(empleado: Empleados_post):
    connection = connection_mysql()
    cursor = connection.cursor()

    # Insertar los datos sin el id (la base de datos lo genera automáticamente)
    query = """
    INSERT INTO empleados (nombre, apellido, email, telefono)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (empleado.nombre, empleado.apellido, empleado.email, empleado.telefono))
    connection.commit()

    # Recuperar el id del nuevo empleado insertado
    new_id = cursor.lastrowid
    cursor.close()
    connection.close()

    # Retornar el empleado con el id generado
    return {"id": new_id, "nombre": empleado.nombre, "apellido": empleado.apellido, "email": empleado.email, "telefono": empleado.telefono}

# metodo para eliminar empleados
@app.delete("/empleados/{id}", response_model=dict)
async def eliminar_empleado(id: int):
    """
    Elimina un empleado por su ID.
    """
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Intentar eliminar el empleado con el ID especificado
            sql = "DELETE FROM empleados WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()

            # Verificar si realmente se eliminó alguna fila
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Empleado no encontrado")
            
            return {"mensaje": f"Empleado con ID {id} eliminado correctamente"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        connection.close()
        
# metodo para actualizar empleados
@app.put("/empleados/{id}", response_model=dict)
async def actualizar_empleado(id: int, empleado: Empleados_post):
    """
    Actualiza los datos de un empleado por su ID.
    """
    connection = connection_mysql()

    try:
        with connection.cursor() as cursor:
            # Actualizar el empleado con los nuevos datos
            sql = """
                UPDATE empleados
                SET nombre = %s, apellido = %s, email = %s, telefono = %s
                WHERE id = %s
            """
            cursor.execute(sql, (empleado.nombre, empleado.apellido, empleado.email, empleado.telefono, id))
            connection.commit()

            # Verificar si realmente se actualizó alguna fila
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Empleado no encontrado")
            
            return {"mensaje": f"Empleado con ID {id} actualizado correctamente"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        connection.close()
        
"################################### CRUD PARA PRODUCTOS #######################################"

# Ruta GET para obtener los datos de todos los productos
@app.get("/productos", response_model=List[Producto])
async def productos():
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
 
 # Método para agregar productos
@app.post("/productos", response_model=dict)
async def crear_producto(producto: Producto_post):
    """
    Agrega un nuevo producto.
    """
    connection = connection_mysql()
    try:
        with connection.cursor() as cursor:
            # Insertar los datos
            query = """
            INSERT INTO productos (nombre, descripcion, precio, cantidad)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (producto.nombre, producto.descripcion, producto.precio, producto.cantidad))
            connection.commit()

            # Recuperar el id del nuevo producto
            new_id = cursor.lastrowid
            
            return {
                "id": new_id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        connection.close()
        
# Método para eliminar productos
@app.delete("/productos/{id}", response_model=dict)
async def eliminar_producto(id: int):
    """
    Elimina un producto por su ID.
    """
    connection = connection_mysql()
    try:
        with connection.cursor() as cursor:
            # Intentar eliminar el producto con el ID especificado
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()

            # Verificar si realmente se eliminó alguna fila
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Producto no encontrado")
            
            return {"mensaje": f"Producto con ID {id} eliminado correctamente"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        connection.close()

# Método para actualizar productos
@app.put("/productos/{id}", response_model=dict)
async def actualizar_producto(id: int, producto: Producto_post):
    """
    Actualiza los datos de un producto por su ID.
    """
    connection = connection_mysql()
    try:
        with connection.cursor() as cursor:
            # Actualizar el producto con los nuevos datos
            sql = """
                UPDATE productos
                SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s
                WHERE id = %s
            """
            cursor.execute(sql, (producto.nombre, producto.descripcion, producto.precio, producto.cantidad, id))
            connection.commit()

            # Verificar si realmente se actualizó alguna fila
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Producto no encontrado")
            
            return {"mensaje": f"Producto con ID {id} actualizado correctamente"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        connection.close()
    
from fastapi.responses import Response

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)
