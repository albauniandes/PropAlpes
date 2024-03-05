"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from enum import Enum
from geograficos.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass


class EstadoDatosGeograficos(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    RECHAZADA = "Rechazada"

@dataclass(frozen=True)
class NombrePropiedad(ObjetoValor):
    nombre_propiedad: str

@dataclass(frozen=True)
class Latitud(ObjetoValor):
    latitud: str

@dataclass(frozen=True)
class Longitud(ObjetoValor):
    longitud: int

