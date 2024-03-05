"""Entidades del dominio de validación y autorización"""

from datetime import datetime
from geograficos.seedwork.dominio.entidades import Entidad
from geograficos.seedwork.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from dataclasses import dataclass, field

from .objetos_valor import EstadoCompania, Nombre, Email, Identificacion

@dataclass
class DatosGeograficos(AgregacionRaiz):
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre_propiedad: ov.NombrePropiedad = field(default=ov.NombrePropiedad)
    latitud: ov.Latitud = field(default=ov.Latitud)
    longitud: ov.Longitud = field(default=ov.Longitud)