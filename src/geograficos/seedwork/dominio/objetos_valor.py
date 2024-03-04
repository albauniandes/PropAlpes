"""Objetos valor reusables parte del seedwork del proyecto"""

from dataclasses import dataclass

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class NombrePropiedad(ObjetoValor):
    nombre_propiedad: str

@dataclass(frozen=True)
class Latitud(ObjetoValor):
    latitud: str

@dataclass(frozen=True)
class Longitud(ObjetoValor):
    longitud: str