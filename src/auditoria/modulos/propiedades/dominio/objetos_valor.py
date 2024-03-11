"""Objetos valor del dominio de propiedades"""

from __future__ import annotations

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Nombre, Identificacion, Email, MotivoAuditoria
from datetime import datetime
from enum import Enum



@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    email: str

@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    identificacion: str


@dataclass(frozen=True)
class MotivoAuditoria(ObjetoValor):
    motivo_auditoria: str