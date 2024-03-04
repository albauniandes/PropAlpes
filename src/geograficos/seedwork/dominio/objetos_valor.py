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
class Pais(ObjetoValor):
    codigo: Codigo
    nombre: str

@dataclass(frozen=True)
class Ciudad(ObjetoValor):
    pais: Pais
    codigo: Codigo
    nombre: str

@dataclass(frozen=True)
class NombrePropiedad(ObjetoValor):
    nombre_propiedad: str

@dataclass(frozen=True)
class Latitud(ObjetoValor):
    latitud: float

@dataclass(frozen=True)
class Longitud(ObjetoValor):
    longitud: float