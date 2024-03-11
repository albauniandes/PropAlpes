from __future__ import annotations
from dataclasses import dataclass, field
from auditoria.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoPropiedades(EventoDominio):
    ...

@dataclass
class PropiedadCreada(EventoPropiedades):
    id_propiedad: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None
    nombre: str = None
    identificacion_catastral: str = None


@dataclass
class CreacionPropiedadFallida(EventoPropiedades):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None
    nombre: str = None
    identificacion_catastral: str = None
@dataclass
class PropiedadEliminada(EventoPropiedades):
    id_propiedad: uuid.UUID = None
    fecha_actualizacion: datetime = None
