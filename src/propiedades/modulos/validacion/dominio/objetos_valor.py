"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from enum import Enum
from propiedades.seedwork.dominio.objetos_valor import ObjetoValor, IdentificacionCatastral, Nit, Nombre
from dataclasses import dataclass


class EstadoPropiedad(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    RECHAZADA = "Rechazada"

@dataclass(frozen=True)
class IdentificacionCatastral(ObjetoValor):
    identificacion_catastral: str

@dataclass(frozen=True)
class Nit(ObjetoValor):
    nit: str

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: int

