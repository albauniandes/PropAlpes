"""Entidades del dominio de ingestion"""

from __future__ import annotations
from dataclasses import dataclass, field

import geograficos.modulos.ingestion.dominio.objetos_valor as ov
from geograficos.modulos.ingestion.dominio.eventos import DatosGeograficosCreados, DatosGeograficosAprobados, DatosGeograficosRechazados
from geograficos.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class DatosGeograficos(AgregacionRaiz):
    estado: ov.EstadoDatosGeograficos = field(default=ov.EstadoDatosGeograficos.PENDIENTE)
    nombre_propiedad: ov.NombrePropiedad = field(default=ov.NombrePropiedad)
    latitud: ov.Latitud = field(default=ov.Latitud)
    longitud: ov.Longitud = field(default=ov.Longitud)

    def crear_datos_geograficos(self, datos_geograficos: DatosGeograficos):
        self.estado = datos_geograficos.estado
        
        self.agregar_evento(DatosGeograficosCreados(id_geograficos=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def aprobar_datos_geograficos(self):
        self.estado = ov.EstadoDatosGeograficos.APROBADA

        self.agregar_evento(DatosGeograficosAprobados(self.id, self.fecha_actualizacion))

    def rechazar_datos_geograficos(self):
        self.estado = ov.EstadoDatosGeograficos.RECHAZADA

        self.agregar_evento(DatosGeograficosRechazados(self.id, self.fecha_actualizacion))