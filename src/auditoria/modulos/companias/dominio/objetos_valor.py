"""Objetos valor del dominio de companias"""

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
    nombre: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    email: str

@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    identificacion: str

