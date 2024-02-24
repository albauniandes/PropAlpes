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

# class Ruta(ABC, ObjetoValor):
#     @abstractmethod
#     def origen(self) -> Locacion:
#         ...
    
#     @abstractmethod
#     def destino(self) -> Locacion:
#         ...
    
#     @abstractmethod
#     def fecha_salida(self) -> datetime:
#         ...

#     @abstractmethod
#     def fecha_llegada(self) -> datetime:
#         ...

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