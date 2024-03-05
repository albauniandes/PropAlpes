from dataclasses import dataclass, field
from geograficos.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class DatosGeograficosDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre_propiedad: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)