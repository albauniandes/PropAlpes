from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class AuditoriaPropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    email: str = field(default_factory=str)
    identificacion: str = field(default_factory=str)
    motivo_auditoria: str = field(default_factory=str)