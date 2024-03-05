""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from auditoria.config.db import db
from auditoria.modulos.companias.dominio.repositorios import (RepositorioAuditoriaCompanias,
                                                              RepositorioEventosAuditoriaCompanias)
from auditoria.modulos.companias.dominio.objetos_valor import EstadoCompania, Nombre, Email, Identificacion
from auditoria.modulos.companias.dominio.entidades import AuditoriaCompania
from auditoria.modulos.companias.dominio.fabricas import FabricaIngestion
from .dto import AuditoriaCompania as AuditoriaCompaniaDTO
from .dto import EventosAuditoriaCompania
from .mapeadores import MapeadorCompania, MapadeadorEventosCompania
from uuid import UUID
from pulsar.schema import *


class RepositorioAuditoriaCompaniasSQLAlchemy(RepositorioAuditoriaCompanias):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> AuditoriaCompania:
        auditoria_compania_dto = db.session.query(AuditoriaCompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapeadorCompania())

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: Compania):
        compania_dto = self.fabrica_ingestion.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)

    def actualizar(self, compania: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosCompaniasSQLAlchemy(RepositorioEventosCompanias):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(compania_dto, MapadeadorEventosCompania())

    def obtener_todos(self) -> list[Compania]:
        raise NotImplementedError

    def agregar(self, evento):
        compania_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosCompania())

        parser_payload = JsonSchema(compania_evento.data.__class__)
        json_str = parser_payload.encode(compania_evento.data)

        evento_dto = EventosCompania()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_compania)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(compania_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(compania_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, compania: Compania):
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        raise NotImplementedError