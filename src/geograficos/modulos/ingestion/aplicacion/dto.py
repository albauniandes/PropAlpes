from dataclasses import dataclass, field
from geograficos.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class DatosGeograficosDTO(DTO):
    nombre_propiedad: str = field(default_factory=str)
    latitud: float = field(default_factory=float)
    longitud: float = field(default_factory=float)
    id: str = field(default_factory=str)