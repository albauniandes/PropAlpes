from __future__ import annotations
from dataclasses import dataclass, field
from auditoria.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoGeograficos(EventoDominio):
    ...

@dataclass
class GeograficoCreado(EventoGeograficos):
    id_geografico: uuid.UUID = None
    id_correlacion: str = None
    latitud: float = None
    longitud: float = None
    fecha_creacion: datetime = None

@dataclass
class CreacionGeograficoFallida(EventoGeograficos):
    id_geografico: uuid.UUID = None
    fecha_creacion: datetime = None
    latitud: float = None
    longitud: float = None



@dataclass
class GeograficoEliminado(EventoGeograficos):
    id_geografico: uuid.UUID = None
    fecha_actualizacion: datetime = None
