""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from auditoria_test.config.db import db
from auditoria_test.modulos.companias.dominio.repositorios import (RepositorioAuditoriaCompanias,
                                                              RepositorioEventosAuditoriaCompanias)
from auditoria_test.modulos.companias.dominio.objetos_valor import MotivoAuditoria, Nombre, Email, Identificacion
from auditoria_test.modulos.companias.dominio.entidades import AuditoriaCompania
from auditoria_test.modulos.companias.dominio.fabricas import FabricaAuditoriaCompania
from .dto import AuditoriaCompania as AuditoriaCompaniaDTO
from .dto import EventosAuditoriaCompania
from .mapeadores import MapeadorAuditoriaCompania, MapadeadorEventosAuditoriaCompania
from uuid import UUID
from pulsar.schema import *


class RepositorioAuditoriaCompaniasSQLAlchemy(RepositorioAuditoriaCompanias):

    def __init__(self):
        self._fabrica_auditoria_compania: FabricaAuditoriaCompania = FabricaAuditoriaCompania()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_auditoria_compania

    def obtener_por_id(self, id: UUID) -> AuditoriaCompania:
        auditoria_compania_dto = db.session.query(AuditoriaCompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapeadorAuditoriaCompania())

    def obtener_todos(self) -> list[AuditoriaCompania]:
        # TODO
        raise NotImplementedError

    def agregar(self, auditoria_compania: AuditoriaCompania):
        compania_dto = self.fabrica_ingestion.crear_objeto(auditoria_compania, MapeadorAuditoriaCompania())
        db.session.add(compania_dto)

    def actualizar(self, auditoria_compania: AuditoriaCompania):
        # TODO
        raise NotImplementedError

    def eliminar(self, auditoria_compania_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosAuditoriaCompaniasSQLAlchemy(RepositorioEventosAuditoriaCompanias):

    def __init__(self):
        self._fabrica_ingestion: FabricaAuditoriaCompania = FabricaAuditoriaCompania()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> AuditoriaCompania:
        auditoria_compania_dto = db.session.query(AuditoriaCompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapadeadorEventosAuditoriaCompania())

    def obtener_todos(self) -> list[AuditoriaCompania]:
        raise NotImplementedError

    def agregar(self, evento):
        auditoria_compania_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosAuditoriaCompania())

        parser_payload = JsonSchema(auditoria_compania_evento.data.__class__)
        json_str = parser_payload.encode(auditoria_compania_evento.data)

        evento_dto = EventosAuditoriaCompania()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_compania)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(auditoria_compania_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(auditoria_compania_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, auditoria_compania: AuditoriaCompania):
        raise NotImplementedError

    def eliminar(self, auditoria_compania_id: UUID):
        raise NotImplementedError