"""Entidades del dominio de ingestion"""

from __future__ import annotations
from dataclasses import dataclass, field

import companias.modulos.ingestion.dominio.objetos_valor as ov
from companias.modulos.ingestion.dominio.eventos import CompaniaCreada, CompaniaAprobada, CompaniaRechazada
from companias.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Compania(AgregacionRaiz):
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.Nombre = field()
    email: ov.Email = field()
    identificacion = ov.Identificacion = field()

    def crear_compania(self, compania: Compania):
        self.estado = compania.estado

        self.agregar_evento(CompaniaCreada(id_compania=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def aprobar_compania(self):
        self.estado = ov.EstadoCompania.APROBADA

        self.agregar_evento(CompaniaAprobada(self.id, self.fecha_actualizacion))

    def rechazar_compania(self):
        self.estado = ov.EstadoCompania.RECHAZADA

        self.agregar_evento(CompaniaRechazada(self.id, self.fecha_actualizacion))