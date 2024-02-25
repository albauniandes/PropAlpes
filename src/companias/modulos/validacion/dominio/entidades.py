"""Entidades del dominio de validación y autorización"""

from datetime import datetime
from companias.seedwork.dominio.entidades import Entidad
from companias.seedwork.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from dataclasses import dataclass, field

from .objetos_valor import EstadoCompania, Nombre, Email, Identificacion

@dataclass
class Compania(AgregacionRaiz):
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.Nombre = field(default=ov.Nombre)
    email: ov.Email = field(default=ov.Email)
    identificacion = ov.Identificacion = field(default=ov.Identificacion)