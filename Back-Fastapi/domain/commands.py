import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Command(BaseModel):
    pass


class ActividadTipo(Command):
    tipo: str
    created_at: Optional[date]


class Actividad(Command):
    nombre: str
    user_id: Optional[uuid.UUID]
    actividadTipo_id: int


class CombustibleGasto(Command):
    user_id: Optional[uuid.UUID]
    fecha: date
    vehiculo_id: int
    empleado_id: int
    actividad_id: int
    lote_id: int
    combustible_id: int
    cantidadDeCombustibleDepositada: float
    created_at: Optional[date]


class CombustibleHistorial(Command):
    fecha: date
    valorUnitario: float
    cantidad: float
    combustible_id: int
    user_id: Optional[uuid.UUID]
    gasto_id: int
    created_at: Optional[date]


class CombustibleInventario(Command):
    tipo: str
    cantidadActual: float


class Empleado(Command):
    nombre: str
    especialidad: str
    user_id: Optional[uuid.UUID]
    created_at: Optional[date]


class EmpleadoActividadRealizada(Command):
    labor: int
    fecha: date
    empleado_id: int
    lote: int
    created_at: Optional[date]


class Vehiculo(Command):
    nombre: str
    created_at: Optional[date]


class Lote(Command):
    nombre: str
    detalle: str
    created_at: Optional[date]


class EmpleadoActividadRealizada(Command):
    labor: int
    fecha: date
    empleado_id: int
    lote: int
    created_at: Optional[date]


class Semilla(Command):
    nombre: str
    created_at: Optional[date]
