"""Entidades del dominio de validación y autorización"""

from datetime import datetime
from companias.seedwork.dominio.entidades import AgregacionRaiz
from geograficos.seedwork.dominio.entidades import Entidad
from geograficos.seedwork.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from dataclasses import dataclass, field
import geograficos.modulos.ingestion.dominio.objetos_valor as ov

from .objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
@dataclass
class DatosGeograficos(AgregacionRaiz):
    estado: ov.EstadoDatosGeograficos = field(default=ov.EstadoCompania.PENDIENTE)
    nombre_propiedad: ov.NombrePropiedad = field(default=ov.NombrePropiedad)
    Latitud: ov.Latitud = field(default=ov.Latitud)
    longitud: ov.Longitud = field(default=ov.Longitud)