# Definir un modelo para los datos del usuario
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
