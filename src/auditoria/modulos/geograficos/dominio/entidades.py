"""Entidades del dominio de propiedades"""

from __future__ import annotations
from dataclasses import dataclass, field

import auditoria.modulos.geograficos.dominio.objetos_valor as ov
from auditoria.modulos.geograficos.dominio.eventos import AuditoriaGeograficoCreada
from auditoria.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class AuditoriaGeografico(AgregacionRaiz):
    motivo_auditoria: ov.MotivoAuditoria = field(default=ov.MotivoAuditoria)
    latitud: ov.Nombre = field(default=ov.Nombre)
    longitud: ov.Email = field(default=ov.Email)
    identificacion: ov.Identificacion = field(default=ov.Identificacion)

    def crear_auditoria_geografico(self, auditoria_geografico: AuditoriaGeografico):
        self.motivo_geografico = auditoria_geografico.motivo_auditoria
        
        self.agregar_evento(AuditoriaGeograficoCreada(id_auditoria=self.id,
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