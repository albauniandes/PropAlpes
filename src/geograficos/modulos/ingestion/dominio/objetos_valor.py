"""Objetos valor del dominio de ingestion"""

from __future__ import annotations

from dataclasses import dataclass, field
from geograficos.seedwork.dominio.objetos_valor import ObjetoValor, NombrePropiedad, Latitud, Longitud
from datetime import datetime
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

