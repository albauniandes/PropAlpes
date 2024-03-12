""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from auditoria.config.db import db
from auditoria.modulos.propiedades.dominio.repositorios import (RepositorioAuditoriaPropiedads,
                                                                RepositorioEventosAuditoriaPropiedads)
from auditoria.modulos.propiedades.dominio.objetos_valor import MotivoAuditoria, Nombre, Email, Identificacion
from auditoria.modulos.propiedades.dominio.entidades import AuditoriaPropiedad
from auditoria.modulos.propiedades.dominio.fabricas import FabricaAuditoriaPropiedad
from .dto import AuditoriaPropiedad as AuditoriaPropiedadDTO
from .dto import EventosAuditoriaPropiedad
from .mapeadores import MapeadorAuditoriaPropiedad, MapadeadorEventosAuditoriaPropiedad
from uuid import UUID
from pulsar.schema import *


class RepositorioAuditoriaPropiedadsSQLAlchemy(RepositorioAuditoriaPropiedads):

    def __init__(self):
        self._fabrica_auditoria_compania: FabricaAuditoriaPropiedad = FabricaAuditoriaPropiedad()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_auditoria_compania

    def obtener_por_id(self, id: UUID) -> AuditoriaPropiedad:
        auditoria_compania_dto = db.session.query(AuditoriaPropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapeadorAuditoriaPropiedad())

    def obtener_todos(self) -> list[AuditoriaPropiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, auditoria_compania: AuditoriaPropiedad):
        compania_dto = self.fabrica_ingestion.crear_objeto(auditoria_compania, MapeadorAuditoriaPropiedad())
        db.session.add(compania_dto)

    def actualizar(self, auditoria_compania: AuditoriaPropiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, auditoria_compania_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosAuditoriaPropiedadsSQLAlchemy(RepositorioEventosAuditoriaPropiedads):

    def __init__(self):
        self._fabrica_ingestion: FabricaAuditoriaPropiedad = FabricaAuditoriaPropiedad()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> AuditoriaPropiedad:
        auditoria_compania_dto = db.session.query(AuditoriaPropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapadeadorEventosAuditoriaPropiedad())

    def obtener_todos(self) -> list[AuditoriaPropiedad]:
        raise NotImplementedError

    def agregar(self, evento):
        auditoria_compania_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosAuditoriaPropiedad())

        parser_payload = JsonSchema(auditoria_compania_evento.data.__class__)
        json_str = parser_payload.encode(auditoria_compania_evento.data)

        evento_dto = EventosAuditoriaPropiedad()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_compania)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(auditoria_compania_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(auditoria_compania_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, auditoria_compania: AuditoriaPropiedad):
        raise NotImplementedError

    def eliminar(self, auditoria_compania_id: UUID):
        raise NotImplementedError