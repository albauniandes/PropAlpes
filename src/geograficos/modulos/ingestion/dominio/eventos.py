from __future__ import annotations
from dataclasses import dataclass, field
from geograficos.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoDatosGeograficos(EventoDominio):
    ...

@dataclass
class CompaniaCreada(EventoDatosGeograficos):
    id: uuid.UUID = None
    nombre_propiedad: str = None
    
@dataclass
class CompaniaRechazada(EventoCompania):
    id: uuid.UUID = None
    nombre_propiedad: str = None

@dataclass
class CompaniaAprobada(EventoCompania):
    id: uuid.UUID = None
    nombre_propiedad: str = None