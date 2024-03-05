from __future__ import annotations
from dataclasses import dataclass, field
from auditoria.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoAuditoriaCompania(EventoDominio):
    ...

@dataclass
class AuditoriaCompaniaCreada(EventoAuditoriaCompania):
    id_compania: uuid.UUID = None
    motivo_auditoria: str = None
    fecha_creacion: datetime = None
