"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from companias.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass


class EstadoCompania(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    RECHAZADA = "Rechazada"

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    email: str

@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    numero: int

