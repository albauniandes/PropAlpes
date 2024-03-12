"""Objetos valor del dominio de ingestion"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedades.seedwork.dominio.objetos_valor import ObjetoValor, IdentificacionCatastral, Nit, Nombre
from datetime import datetime
from enum import Enum

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
    nombre: str

