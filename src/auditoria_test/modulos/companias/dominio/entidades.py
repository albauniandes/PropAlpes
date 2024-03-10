"""Entidades del dominio de companias"""

from __future__ import annotations
from dataclasses import dataclass, field

import auditoria_test.modulos.companias.dominio.objetos_valor as ov
from auditoria_test.modulos.companias.dominio.eventos import AuditoriaCompaniaCreada
from auditoria_test.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class AuditoriaCompania(AgregacionRaiz):
    motivo_auditoria: ov.MotivoAuditoria = field(default=ov.MotivoAuditoria)
    nombre: ov.Nombre = field(default=ov.Nombre)
    email: ov.Email = field(default=ov.Email)
    identificacion: ov.Identificacion = field(default=ov.Identificacion)

    def crear_auditoria_compania(self, auditoria_compania: AuditoriaCompania):
        self.motivo_auditoria = auditoria_compania.motivo_auditoria
        
        self.agregar_evento(AuditoriaCompaniaCreada(id_compania=self.id,
                                                    motivo_auditoria=self.motivo_auditoria,
                                                    fecha_creacion=self.fecha_creacion))

    # def aprobar_compania(self):
    #     self.estado = ov.EstadoCompania.APROBADA
    #
    #     self.agregar_evento(CompaniaAprobada(self.id, self.fecha_actualizacion))
    #
    # def rechazar_compania(self):
    #     self.estado = ov.EstadoCompania.RECHAZADA
    #
    #     self.agregar_evento(CompaniaRechazada(self.id, self.fecha_actualizacion))