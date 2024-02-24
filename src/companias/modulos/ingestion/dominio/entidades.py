"""Entidades del dominio de ingestion"""

from __future__ import annotations
from dataclasses import dataclass, field

import companias.modulos.ingestion.dominio.objetos_valor as ov
from companias.modulos.ingestion.dominio.eventos import CompaniaCreada, CompaniaAprobada, CompaniaRechazada
from companias.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

# @dataclass
# class Aeropuerto(Locacion):
#     codigo: ov.Codigo = field(default_factory=ov.Codigo)
#     nombre: ov.NombreAero = field(default_factory=ov.NombreAero)

#     def __str__(self) -> str:
#         return self.codigo.codigo.upper()

# @dataclass
# class Proveedor(Entidad):
#     codigo: ov.Codigo = field(default_factory=ov.Codigo)
#     nombre: ov.NombreAero = field(default_factory=ov.NombreAero)
#     itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

#     def obtener_itinerarios(self, odos: list[Odo], parametros: ParametroBusca):
#         return self.itinerarios

# @dataclass
# class Pasajero(Entidad):
#     clase: ov.Clase = field(default_factory=ov.Clase)
#     tipo: ov.TipoPasajero = field(default_factory=ov.TipoPasajero)

@dataclass
class Compania(AgregacionRaiz):
    # id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.Nombre = field()
    email: ov.Email = field()
    identificacion = ov.Identificacion = field()
    # itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def crear_compania(self, compania: Compania):
        # self.id_cliente = compania.id_cliente
        self.estado = compania.estado
        # self.itinerarios = compania.itinerarios

        self.agregar_evento(CompaniaCreada(id_compania=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def aprobar_compania(self):
        self.estado = ov.EstadoCompania.APROBADA

        self.agregar_evento(CompaniaAprobada(self.id, self.fecha_actualizacion))

    def rechazar_compania(self):
        self.estado = ov.EstadoCompania.RECHAZADA

        self.agregar_evento(CompaniaRechazada(self.id, self.fecha_actualizacion))