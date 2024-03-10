"""Entidades del dominio de validación y autorización"""

from datetime import datetime
from auditoria.seedwork.dominio.entidades import AgregacionRaiz
from propiedades.seedwork.dominio.entidades import Entidad
from propiedades.seedwork.dominio.objetos_valor import EstadoPropiedad, IdentificacionCatastral, Nit, Nombre
from dataclasses import dataclass, field
import propiedades.modulos.ingestion.dominio.objetos_valor as ov
from .objetos_valor import EstadoPropiedad, IdentificacionCatastral, Nit, Nombre

@dataclass
class Propiedad(AgregacionRaiz):
    estado: ov.EstadoCompania = field(default=ov.EstadoPropiedad.PENDIENTE)
    identificacion_catastral: ov.IdentificacionCatastral = field(default=ov.IdentificacionCatastral)
    nit: ov.Nit = field(default=ov.Nit)
    nombre: ov.Nombre = field(default=ov.Nombre)