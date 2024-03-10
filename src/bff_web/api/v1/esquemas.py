import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

GEOGRAFICOS_HOST = os.getenv("GEOGRAFICOS_ADDRESS", default="localhost")
COMPANIAS_HOST = os.getenv("COMPANIAS_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_companias(root) -> typing.List["Compania"]:
    companias_json = requests.get(f'http://{COMPANIAS_HOST}:5000/ingestion/compania-query').json()
    companias = []

    for compania in companias_json:
        companias.append(
            Compania(
                fecha_creacion=datetime.strptime(compania.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(compania.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=compania.get('id'), 
                email=compania.get('email'),
                nombre=compania.get('nombre'),
                identificacion=compania.get('identificacion')
            )
        )

    return companias

def obtener_datos_geograficos(root) -> typing.List["DatosGeograficos"]:
    datos_geograficos_json = requests.get(f'http://{GEOGRAFICOS_HOST}:5000/ingestion/datos-geograficos-query').json()
    datos_geograficos = []

    for datos_geograficos in datos_geograficos_json:
        datos_geograficos.append(
            DatosGeograficos(
                fecha_creacion=datetime.strptime(datos_geograficos.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(datos_geograficos.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=datos_geograficos.get('id'), 
                nombre_propiedad=datos_geograficos.get('nombre_propiedad'),
                latitud=datos_geograficos.get('latitud'),
                longitud=datos_geograficos.get('longitud')
            )
        )

    return datos_geograficos


@strawberry.type
class Compania:
    id: str
    nombre: str
    email: str
    identificacion: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class CreacionCompaniaRespuesa:
    mensaje: str
    codigo: int

@strawberry.type
class DatosGeograficos:
    id: str
    nombre_propiedad: str
    latitud: str
    longitud: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class DatosPropiedad:
    id: str
    nombre: str
    nit: str
    identificacion_catastral: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class CreacionDatosPropiedadRespuesta:
    mensaje: str
    codigo: int






