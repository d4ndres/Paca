import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    pass


class EmpleadoActividadRealizada(Event):
    labor: int
    fecha: date
    empleado: str
    actividad: str
    lote: str
    semilla:str
    created_at: Optional[date]
