"""Objetos valor del dominio de ingestion"""

from __future__ import annotations

from dataclasses import dataclass, field
from companias.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Nombre, Identificacion, Email
from datetime import datetime
from enum import Enum

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
    address: str
    dominio: str

@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    numero: int

