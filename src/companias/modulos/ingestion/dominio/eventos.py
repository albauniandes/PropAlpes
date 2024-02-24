from __future__ import annotations
from dataclasses import dataclass, field
from companias.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaCreada(EventoDominio):
    id_compania: uuid.UUID = None
    # id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class CompaniaRechazada(EventoDominio):
    id_compania: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class CompaniaAprobada(EventoDominio):
    id_compania: uuid.UUID = None
    fecha_actualizacion: datetime = None