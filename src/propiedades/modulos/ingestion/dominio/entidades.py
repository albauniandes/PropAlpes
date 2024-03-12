"""Entidades del dominio de ingestion"""

from __future__ import annotations
from dataclasses import dataclass, field

import propiedades.modulos.ingestion.dominio.objetos_valor as ov
from propiedades.modulos.ingestion.dominio.eventos import PropiedadCreada, PropiedadAprobada, PropiedadRechazada
from propiedades.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Propiedad(AgregacionRaiz):
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.PENDIENTE)
    identificacion_catastral: ov.IdentificacionCatastral = field(default=ov.IdentificacionCatastral)
    nit: ov.Nit = field(default=ov.Nit)
    nombre: ov.Nombre = field(default=ov.Nombre)

    def crear_propiedad(self, propiedad: Propiedad):
        self.estado = propiedad.estado
        
        self.agregar_evento(PropiedadCreada(id_propiedad=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion, identificacion_catastral=self.identificacion_catastral, nit=self.nit, nombre=self.nombre))

    def aprobar_propiedad(self):
        self.estado = ov.EstadoPropiedad.APROBADA

        self.agregar_evento(PropiedadAprobada(self.id, self.fecha_actualizacion))

    def rechazar_propiedad(self):
        self.estado = ov.EstadoPropiedad.RECHAZADA

        self.agregar_evento(PropiedadRechazada(self.id, self.fecha_actualizacion))