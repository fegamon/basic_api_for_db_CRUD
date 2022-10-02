from typing import Optional
from pydantic import BaseModel


class tableSchema(BaseModel):
    id: Optional[str]
    name: str
    last_name: str
    age: int
    phone:int
    email: str
