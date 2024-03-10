"""Entidades del dominio de propiedades"""

from __future__ import annotations
from dataclasses import dataclass, field

import auditoria.modulos.propiedades.dominio.objetos_valor as ov
from auditoria.modulos.propiedades.dominio.eventos import AuditoriaPropiedadCreada
from auditoria.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class AuditoriaPropiedad(AgregacionRaiz):
    motivo_auditoria: ov.MotivoAuditoria = field(default=ov.MotivoAuditoria)
    nombre: ov.Nombre = field(default=ov.Nombre)
    email: ov.Email = field(default=ov.Email)
    identificacion: ov.Identificacion = field(default=ov.Identificacion)

    def crear_auditoria_propiedad(self, auditoria_propiedad: AuditoriaPropiedad):
        self.motivo_auditoria = auditoria_propiedad.motivo_auditoria
        
        self.agregar_evento(AuditoriaPropiedadCreada(id_propiedad=self.id,
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