from __future__ import annotations
from dataclasses import dataclass, field
from auditoria.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoAuditoriaGeografico(EventoDominio):
    ...

@dataclass
class AuditoriaGeograficoCreada(EventoAuditoriaGeografico):
    id_auditoria: uuid.UUID = None
    motivo_auditoria: str = None
    fecha_creacion: datetime = None

@dataclass
class CreacionAuditoriaGeograficoFallida(EventoAuditoriaGeografico):
    id_auditoria: uuid.UUID = None
    fecha_creacion: datetime = None
    motivo_auditoria: str = None