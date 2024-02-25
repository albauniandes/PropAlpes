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
class Direccion(ObjetoValor):
    direccion: str

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    identificacion: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    email: str