from typing import Optional
from pydantic import BaseModel


class studentSchema(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    edad: int
    cedula: str
    email: str
    genero: str
