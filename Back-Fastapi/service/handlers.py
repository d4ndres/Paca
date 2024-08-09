from typing import List

from config.db_config import supabase
from domain import events, commands
from Exceptions.exceptions import CustomException


def create_actividadtipo(actividadtipo: commands.ActividadTipo):
    try:
        response, count = supabase.table('ActividadTipo').insert(
            {
                "tipo": f"{actividadtipo.tipo}",
                "created_at": f"{actividadtipo.created_at}"
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear actividad tipo: {str(e)}")


def create_combustiblegasto(combustiblegasto: commands.CombustibleGasto):
    try:
        response, count = supabase.table('CombustibleGasto').insert(
            {
                "user_id": f"{combustiblegasto.user_id}",
                "fecha": f"{combustiblegasto.fecha}",
                "vehiculo_id": f"{combustiblegasto.vehiculo_id}",
                "empleado_id": f"{combustiblegasto.empleado_id}",
                "actividad_id": f"{combustiblegasto.actividad_id}",
                "lote_id": f"{combustiblegasto.lote_id}",
                "combustible_id": f"{combustiblegasto.combustible_id}",
                "cantidadDeCombustibleDepositada": f"{combustiblegasto.cantidadDeCombustibleDepositada}",
                "created_at": f"{combustiblegasto.created_at}"
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear combustible gasto: {str(e)}")


def create_combustibleinventario(combustibleinventario: commands.CombustibleInventario):
    try:
        response, count = supabase.table('CombustibleInventario').insert(
            {
                "tipo": f"{combustibleinventario.tipo}",
                "cantidadActual": f"{combustibleinventario.cantidadActual}"
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear combustible inventario: {str(e)}")


def create_empleado(empleados: List[commands.Empleado]):
    try:

        data = [
            {
                "nombre": f"{empleado.nombre}",
                "especialidad": f"{empleado.especialidad}",
                "user_id": f"{empleado.user_id}",
                "created_at": f"{empleado.created_at}"
            } for empleado in empleados
        ]
        response, count = supabase.table('Empleado').insert(data).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear empleado: {str(e)}")


def create_lote(lotes: List[commands.Lote]):
    try:
        data = [
            {
                "nombre": f"{lote.nombre}",
                "detalle": f"{lote.detalle}",
                "created_at": f"{lote.created_at}"
            } for lote in lotes
        ]

        response, count = supabase.table('Lote').insert(data).execute().onrender.com
        return response
    except Exception as e:
        raise CustomException(f"Error al crear lote: {str(e)}")


def create_vehiculo(vehiculos: List[commands.Vehiculo]):
    try:
        data = [
            {
                "nombre": f"{vehiculo.nombre}",
                "created_at": f"{vehiculo.created_at}"
            } for vehiculo in vehiculos
        ]
        response, count = supabase.table('Vehiculo').insert(data).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear vehiculo: {str(e)}")


def update_activity(actividad_id: int, actividad: commands.Actividad):
    try:
        response, _ = supabase.table("Actividad").update({
            "nombre": f"{actividad.nombre}",
            "user_id": f"{actividad.user_id}",
            "actividadTipo_id": f"{actividad.actividadTipo_id}"
        }).eq("id", actividad_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar actividad: {str(e)}")


def get_vehiculo_id(vehiculo_id):
    try:
        response = supabase.table('Vehiculo').select("*").eq('id', vehiculo_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener vehiculo por id: {str(e)}")


def get_vehiculo():
    try:
        response = supabase.table('Vehiculo').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener vehiculo: {str(e)}")


def get_lote_id(lote_id):
    try:
        response = supabase.table('Lote').select("*").eq('id', lote_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener lote por id: {str(e)}")


def get_lote():
    try:
        response = supabase.table('Lote').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener lote: {str(e)}")


def get_empleado_id(empleado_id):
    try:
        response = supabase.table('Empleado').select("*").eq('id', empleado_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener empleado por id: {str(e)}")


def get_empleado():
    try:
        response = supabase.table('Empleado').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener empleado: {str(e)}")


def get_combustibleinventario():
    try:
        response = supabase.table('CombustibleInventario').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener combustible inventario: {str(e)}")


def get_combustibleHistorial():
    try:
        response = supabase.table('CombustibleHistorial').select(
            "id",
            "created_at",
            "fecha",
            "valorUnitario",
            "cantidad",
            "gasto_id",
            "combustible_id",
            "user_id",
            "Gasto:gasto_id(nombre)",
            "Combustible:combustible_id(nombre)",
            "cantidadDeCombustibleDepositada"
            "Actividad:actividad_id(nombre)",
            "Lote:lote_id(nombre)",
            "Empleado:user_id(nombre)"
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener combustible historial: {str(e)}")


def get_combustiblegasto_id(combustiblegasto_id):
    try:
        response = supabase.table('CombustibleGasto').select("*").eq('id', combustiblegasto_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener combustible gasto por id: {str(e)}")


def get_combustiblegasto():
    try:
        response = supabase.table('CombustibleGasto').select(
            "id",
            "created_at",
            "fecha",
            "actividad_id",
            "lote_id",
            "empleado_id",
            "combustible_id",
            "user_id",
            "Empleado:empleado_id(nombre)",
            "Combustible:combustible_id(nombre)",
            "cantidadDeCombustibleDepositada"
            "Actividad:actividad_id(nombre)",
            "Lote:lote_id(nombre)",
            "Empleado:user_id(nombre)"
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener combustible gasto: {str(e)}")


def get_actividadtipos():
    try:
        response = supabase.table('ActividadTipo').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener actividad tipo: {str(e)}")


def create_activities(actividad):
    try:
        response, count = supabase.table('Actividad').insert(
            {
                "nombre": f"{actividad.nombre}",
                "user_id": f"{actividad.user_id}",
                "actividadTipo_id": f"{actividad.actividadTipo_id}"
            }
        ).execute()

        return response
    except Exception as e:
        raise CustomException(f"Error al crear actividad: {str(e)}")


def get_activities():
    try:
        response = supabase.table('Actividad').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener actividad: {str(e)}")


def update_actividadtipo(actividadtipo, actividadtipo_id):
    try:
        response, _ = supabase.table("ActividadTipo").update({
            "tipo": f"{actividadtipo.tipo}",
            "created_at": f"{actividadtipo.created_at}"
        }).eq("id", actividadtipo_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar actividad tipo: {str(e)}")


def update_combustiblegasto(combustiblegasto_id, combustiblegasto):
    try:
        response, _ = supabase.table("CombustibleGasto").update({
            "user_id": f"{combustiblegasto.user_id}",
            "fecha": f"{combustiblegasto.fecha}",
            "vehiculo_id": f"{combustiblegasto.vehiculo_id}",
            "empleado_id": f"{combustiblegasto.empleado_id}",
            "actividad_id": f"{combustiblegasto.actividad_id}",
            "lote_id": f"{combustiblegasto.lote_id}",
            "combustible_id": f"{combustiblegasto.combustible_id}",
            "cantidadDeCombustibleDepositada": f"{combustiblegasto.cantidadDeCombustibleDepositada}",
            "created_at": f"{combustiblegasto.created_at}"
        }).eq("id", combustiblegasto_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar combustible gasto: {str(e)}")


def update_combustibleinventario(combustibleinventario_id, combustibleinventario):
    try:
        response, _ = supabase.table("CombustibleInventario").update({
            "tipo": f"{combustibleinventario.tipo}",
            "cantidadActual": f"{combustibleinventario.cantidadActual}"
        }).eq("id", combustibleinventario_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar combustible inventario: {str(e)}")


def update_empleado(empleado_id, empleado):
    try:
        response, _ = supabase.table("Empleado").update({
            "nombre": f"{empleado.nombre}",
            "especialidad": f"{empleado.especialidad}",
            "user_id": f"{empleado.user_id}",
            "created_at": f"{empleado.created_at}"
        }).eq("id", empleado_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar empleado: {str(e)}")


def update_lote(lote_id, lote):
    try:
        response, _ = supabase.table("Lote").update({
            "nombre": f"{lote.nombre}",
            "detalle": f"{lote.detalle}",
            "created_at": f"{lote.created_at}"
        }).eq("id", lote_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al actualizar lote: {str(e)}")


def get_actividadrealizada():
    try:
        response = supabase.table('EmpleadoActividadRealizada').select(
            "id",
            "created_at",
            "fecha",
            "actividad_id",
            "lote_id",
            "empleado_id",
            "semilla_id",
            "Empleado:empleado_id(nombre)",
            "Actividad:actividad_id(nombre)",
            "Lote:lote_id(nombre)",
            "Semilla:semilla_id(nombre)"
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener actividad realizada: {str(e)}")


def create_actividadrealizada(actividadrealizada: commands.EmpleadoActividadRealizada):
    try:
        response, count = supabase.table('EmpleadoActividadRealizada').insert(
            {
                "empleado_id": f"{actividadrealizada.empleado_id}",
                "lote_id": f"{actividadrealizada.lote}",
                "fecha": f"{actividadrealizada.fecha}",
                "semilla_id": f"{actividadrealizada.labor}",
                "actividad_id": f"{actividadrealizada.actividad_id}",
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear actividad realizada: {str(e)}")


def get_actividadrealizada_id(actividadrealizada_id: int):
    try:
        response = supabase.table('EmpleadoActividadRealizada').select(
            "id",
            "created_at",
            "fecha",
            "actividad_id",
            "lote_id",
            "empleado_id",
            "semilla_id",
            "Empleado:empleado_id(nombre)",
            "Actividad:actividad_id(nombre)",
            "Lote:lote_id(nombre)",
            "Semilla:semilla_id(nombre)"
        ).eq('id', actividadrealizada_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener actividad realizada por id: {str(e)}")


def get_semillas():
    try:
        response = supabase.table('Semilla').select("*").execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener semilla: {str(e)}")


def get_semillas_id(semilla_id):
    try:
        response = supabase.table('Semilla').select("*").eq('id', semilla_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener semilla por id: {str(e)}")


def create_semillas(semilla: commands.Semilla):
    try:
        response, count = supabase.table('Semilla').insert(
            {
                "nombre": f"{semilla.nombre}"
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear semilla: {str(e)}")


def create_combustiblehistorial(combustiblehistorial):
    try:
        response, count = supabase.table('CombustibleHistorial').insert(
            {
                "fecha": f"{combustiblehistorial.fecha}",
                "valorUnitario": f"{combustiblehistorial.valorUnitario}",
                "cantidad": f"{combustiblehistorial.cantidad}",
                "combustible_id": f"{combustiblehistorial.combustible_id}",
                "user_id": f"{combustiblehistorial.user_id}",
                "gasto_id": f"{combustiblehistorial.gasto_id}",
                "created_at": f"{combustiblehistorial.created_at}"
            }
        ).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al crear combustible historial: {str(e)}")


def get_combustiblehistorial_id(combustiblehistorial_id):
    try:
        response = supabase.table('CombustibleHistorial').select(
            "id",
            "created_at",
            "fecha",
            "valorUnitario",
            "cantidad",
            "gasto_id",
            "combustible_id",
            "user_id",
            "Gasto:gasto_id(nombre)",
            "Combustible:combustible_id(nombre)",
            "cantidadDeCombustibleDepositada"
            "Actividad:actividad_id(nombre)",
            "Lote:lote_id(nombre)",
            "Empleado:user_id(nombre)").eq('id', combustiblehistorial_id).execute()
        return response
    except Exception as e:
        raise CustomException(f"Error al obtener combustible historial por id: {str(e)}")