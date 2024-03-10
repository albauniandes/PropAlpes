from __future__ import annotations
from dataclasses import dataclass, field
from propiedades.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoPropiedad(EventoDominio):
    ...

@dataclass
class PropiedadCreada(EventoPropiedad):
    id_propiedad: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class PropiedadRechazada(EventoPropiedad):
    id_propiedad: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class PropiedadAprobada(EventoPropiedad):
    id_propiedad: uuid.UUID = None
    fecha_actualizacion: datetime = None