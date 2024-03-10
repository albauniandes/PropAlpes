""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from auditoria.config.db import db
from auditoria.modulos.geograficos.dominio.repositorios import ( RepositorioAuditoriaGeograficos,
                                                                RepositorioEventosAuditoriaGeograficos)
from auditoria.modulos.geograficos.dominio.objetos_valor import MotivoAuditoria, Nombre, Email, Identificacion
from auditoria.modulos.geograficos.dominio.entidades import AuditoriaGeografico
from auditoria.modulos.geograficos.dominio.fabricas import FabricaAuditoriaGeografico
from .dto import AuditoriaGeografico as AuditoriaGeograficoDTO
from .dto import EventosAuditoriaGeografico
from .mapeadores import MapeadorAuditoriaGeografico, MapadeadorEventosAuditoriaGeografico
from uuid import UUID
from pulsar.schema import *


class RepositorioAuditoriaGeograficosSQLAlchemy(RepositorioAuditoriaGeograficos):

    def __init__(self):
        self._fabrica_auditoria_geograficos: FabricaAuditoriaGeografico = FabricaAuditoriaGeografico()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_auditoria_geograficos

    def obtener_por_id(self, id: UUID) -> AuditoriaGeografico:
        auditoria_geografico_dto = db.session.query(AuditoriaGeograficoDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_geografico_dto, MapeadorAuditoriaGeografico())

    def obtener_todos(self) -> list[AuditoriaGeografico]:
        # TODO
        raise NotImplementedError

    def agregar(self, auditoria_geografico: AuditoriaGeografico):
        geografico_dto = self.fabrica_ingestion.crear_objeto(auditoria_geografico, MapeadorAuditoriaGeografico())
        db.session.add(geografico_dto)

    def actualizar(self, auditoria_compania: AuditoriaGeografico):
        # TODO
        raise NotImplementedError

    def eliminar(self, auditoria_compania_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosAuditoriaGeograficosSQLAlchemy(RepositorioEventosAuditoriaGeograficos):

    def __init__(self):
        self._fabrica_ingestion: FabricaAuditoriaGeografico = FabricaAuditoriaGeografico()


    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> AuditoriaGeografico:
        auditoria_gegrafico_dto = db.session.query(AuditoriaGeograficoDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(auditoria_gegrafico_dto, MapadeadorEventosAuditoriaGeografico())

    def obtener_todos(self) -> list[AuditoriaGeografico]:
        raise NotImplementedError

    def agregar(self, evento):
        auditoria_compania_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosAuditoriaGeografico())

        parser_payload = JsonSchema(auditoria_compania_evento.data.__class__)
        json_str = parser_payload.encode(auditoria_compania_evento.data)

        evento_dto = EventosAuditoriaGeografico()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_compania)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(auditoria_compania_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(auditoria_compania_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, auditoria_geografico: AuditoriaGeografico):
        raise NotImplementedError

    def eliminar(self, auditoria_geografico_id: UUID):
        raise NotImplementedError