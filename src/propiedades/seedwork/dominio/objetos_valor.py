"""Objetos valor reusables parte del seedwork del proyecto"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):
    codigo: str

@dataclass(frozen=True)
class IdentificacionCatastral(ObjetoValor):
    identificacion_catastral: str

@dataclass(frozen=True)
class Nit(ObjetoValor):
    nit: str

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str