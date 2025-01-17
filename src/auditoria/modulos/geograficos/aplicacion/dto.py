from dataclasses import dataclass, field
from companias.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class AuditoriaGeograficoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)
    identificacion: str = field(default_factory=str)
    motivo_auditoria: str = field(default_factory=str)