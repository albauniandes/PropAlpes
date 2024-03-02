from __future__ import annotations
from dataclasses import dataclass, field
from companias.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoCompania(EventoDominio):
    ...

@dataclass
class CompaniaCreada(EventoCompania):
    id_compania: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class CompaniaRechazada(EventoCompania):
    id_compania: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class CompaniaAprobada(EventoCompania):
    id_compania: uuid.UUID = None
    fecha_actualizacion: datetime = None