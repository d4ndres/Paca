from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from domain import commands
from service import handlers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "¡Api APPA!"}


@app.get("/actividad")
def activities():
    try:
        response = handlers.get_activities()
        return response
    except Exception as e:
        raise e


@app.post("/actividad")
def actividad(actividad: commands.Actividad):
    try:
        response = handlers.create_activities(actividad)
        return response
    except Exception as e:
        raise e


@app.put("/actividad/{actividad_id}")
def actividad(actividad_id: int, actividad: commands.Actividad):
    try:
        handlers.update_activity(actividad_id=actividad_id, actividad=actividad)
        return {"message": f"Actualizando la actividad {actividad_id}"}
    except Exception as e:
        raise e


@app.post("/Tipoactividad/")
def tipoactividad(actividadtipo: commands.ActividadTipo):
    try:
        response = handlers.create_actividadtipo(actividadtipo)
        return response
    except Exception as e:
        raise e


@app.put("/Tipoactividad/{actividadtipo_id}")
def tipoactividad(actividadtipo: commands.ActividadTipo, actividadtipo_id: int):
    try:
        response = handlers.update_actividadtipo(actividadtipo, actividadtipo_id)
        return response
    except Exception as e:
        raise e


@app.get("/ActividadRealizada/")
def actividadrealizada():
    try:
        response = handlers.get_actividadrealizada()
        return response
    except Exception as e:
        raise e


@app.get("/Semillla/")
def semilla():
    try:
        response = handlers.get_semillas()
        return response
    except Exception as e:
        raise e


@app.get("/Semillla/{semilla_id}")
def semilla(semilla_id: int):
    try:
        response = handlers.get_semillas_id(semilla_id)
        return response
    except Exception as e:
        raise e


@app.post("/Semillla/")
def semilla(semilla: commands.Semilla):
    try:
        response = handlers.create_semillas(semilla)
        return response
    except Exception as e:
        raise e


@app.get("/ActividadRealizada/{actividadrealizada_id}")
def actividadrealizada(actividadrealizada_id: int):
    try:
        response = handlers.get_actividadrealizada_id(actividadrealizada_id)
        return response
    except Exception as e:
        raise e


@app.post("/ActividadRealizada/")
def actividadrealizada(actividadrealizada: commands.EmpleadoActividadRealizada):
    try:
        response = handlers.create_actividadrealizada(actividadrealizada)
        return response
    except Exception as e:
        raise e


@app.get("/Tipoactividad")
def tipoactividad():
    try:
        response = handlers.get_actividadtipos()
        return response
    except Exception as e:
        raise e


@app.post("/CombustibleGasto")
def combustiblegasto(combustiblegasto: commands.CombustibleGasto):
    try:
        response = handlers.create_combustiblegasto(combustiblegasto)
        return response
    except Exception as e:
        raise e


@app.put("/CombustibleGasto/{combustiblegasto_id}")
def combustiblegasto(combustiblegasto_id: int, combustiblegasto: commands.CombustibleGasto):
    try:
        response = handlers.update_combustiblegasto(combustiblegasto_id, combustiblegasto)
        return response
    except Exception as e:
        raise e


@app.get("/CombustibleGasto")
def combustiblegasto():
    try:
        response = handlers.get_combustiblegasto()
        return response
    except Exception as e:
        raise e


@app.get("/CombustibleGasto/{combustiblegasto_id}")
def combustiblegasto(combustiblegasto_id: int):
    try:
        response = handlers.get_combustiblegasto_id(combustiblegasto_id)
        return response
    except Exception as e:
        raise e


@app.get("/CombustibleInventario")
def combustibleinventario():
    try:
        response = handlers.get_combustibleinventario()
        return response
    except Exception as e:
        raise e


@app.put("/CombustibleInventario/{combustibleinventario_id}")
def combustibleinventario(combustibleinventario_id: int, combustibleinventario: commands.CombustibleInventario):
    try:
        response = handlers.update_combustibleinventario(combustibleinventario_id, combustibleinventario)
        return response
    except Exception as e:
        raise e


@app.post("/CombustibleInventario")
def combustibleinventario(combustibleinventario: commands.CombustibleInventario):
    try:
        response = handlers.create_combustibleinventario(combustibleinventario)
        return response
    except Exception as e:
        raise e


@app.get("/Empleado")
def empleado():
    try:
        response = handlers.get_empleado()
        return response
    except Exception as e:
        raise e


@app.post("/Empleado")
def empleado(empleado: List[commands.Empleado]):
    try:
        response = handlers.create_empleado(empleado)
        return response
    except Exception as e:
        raise e


@app.put("/Empleado/{empleado_id}")
def empleado(empleado_id: int, empleado: commands.Empleado):
    try:
        response = handlers.update_empleado(empleado_id, empleado)
        return response
    except Exception as e:
        raise e


@app.get("/Empleado/{empleado_id}")
def empleado(empleado_id: int):
    try:
        response = handlers.get_empleado_id(empleado_id)
        return response
    except Exception as e:
        raise e


@app.get("/Lote")
def lote():
    try:
        response = handlers.get_lote()
        return response
    except Exception as e:
        raise e


@app.put("/Lote/{lote_id}")
def lote(lote_id: int, lote: commands.Lote):
    try:
        response = handlers.update_lote(lote_id, lote)
        return response
    except Exception as e:
        raise e


@app.post("/Lote")
def lote(lote: List[commands.Lote]):
    try:
        response = handlers.create_lote(lote)
        return response
    except Exception as e:
        raise e


@app.get("/Lote/{lote_id}")
def lote(lote_id: int):
    try:
        response = handlers.get_lote_id(lote_id)
        return response
    except Exception as e:
        raise e


@app.get("/Vehiculo")
def vehiculo():
    try:
        response = handlers.get_vehiculo()
        return response
    except Exception as e:
        raise e


@app.post("/Vehiculo")
def vehiculo(vehiculo: List[commands.Vehiculo]):
    try:
        response = handlers.create_vehiculo(vehiculo)
        return response
    except Exception as e:
        raise e


@app.put("/Vehiculo/{vehiculo_id}")
def vehiculo(vehiculo_id: int, vehiculo: commands.Vehiculo):
    try:
        response = handlers.update_vehiculo(vehiculo_id, vehiculo)
        return response
    except Exception as e:
        raise e


@app.get("/Vehiculo/{vehiculo_id}")
def vehiculo(vehiculo_id: int):
    try:
        response = handlers.get_vehiculo_id(vehiculo_id)
        return response
    except Exception as e:
        raise e
