from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    identificacion_catastral: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    nombre: str = field(default_factory=str)