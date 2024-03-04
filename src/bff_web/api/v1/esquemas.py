import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


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






