from __future__ import annotations
from dataclasses import dataclass, field
from geograficos.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoDatosGeograficos(EventoDominio):
    ...

@dataclass
class DatosGeograficosCreados(EventoDatosGeograficos):
    id_geograficos: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    nombre_propiedad: str = None
    latitud: str = None
    longitud: str = None
    
@dataclass
class DatosGeograficosRechazados(EventoDatosGeograficos):
    id_geograficos: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class DatosGeograficosAprobados(EventoDatosGeograficos):
    id_geograficos: uuid.UUID = None
    fecha_actualizacion: datetime = None