"""Entidades del dominio de companias"""

from __future__ import annotations
from dataclasses import dataclass, field

import companias.modulos.ingestion.dominio.objetos_valor as ov
from companias.modulos.ingestion.dominio.eventos import CompaniaCreada, CompaniaAprobada, CompaniaRechazada
from companias.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class AuditoriaCompania(AgregacionRaiz):
    motivo: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.Nombre = field(default=ov.Nombre)
    email: ov.Email = field(default=ov.Email)
    identificacion: ov.Identificacion = field(default=ov.Identificacion)

    def crear_auditoria_compania(self, auditoria_compania: AuditoriaCompania):
        self.estado = auditoria_compania.estado
        
        self.agregar_evento(CompaniaCreada(id_compania=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def aprobar_compania(self):
        self.estado = ov.EstadoCompania.APROBADA

        self.agregar_evento(CompaniaAprobada(self.id, self.fecha_actualizacion))

    def rechazar_compania(self):
        self.estado = ov.EstadoCompania.RECHAZADA

        self.agregar_evento(CompaniaRechazada(self.id, self.fecha_actualizacion))