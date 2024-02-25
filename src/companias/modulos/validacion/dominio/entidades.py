"""Entidades del dominio de validación y autorización"""

from datetime import datetime
from companias.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field

from .objetos_valor import *

@dataclass
class Compania(AgregacionRaiz):
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.Nombre = field()
    email: ov.Email = field()
    identificacion = ov.Identificacion = field()