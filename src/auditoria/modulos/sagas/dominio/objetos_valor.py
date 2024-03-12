"""Objetos valor del dominio de ingestion"""

from __future__ import annotations

from dataclasses import dataclass
from geograficos.seedwork.dominio.objetos_valor import ObjetoValor
from enum import Enum

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
    longitud: str


@dataclass(frozen=True)
class IdentificacionCatastral(ObjetoValor):
    identificacion_catastral: str


@dataclass(frozen=True)
class Nit(ObjetoValor):
    nit: str