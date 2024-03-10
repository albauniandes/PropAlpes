""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from propiedades.config.db import db
from propiedades.modulos.ingestion.dominio.repositorios import RepositorioPropiedad, RepositorioEventosPropiedad
from propiedades.modulos.ingestion.dominio.objetos_valor import EstadoPropiedad, IdentificacionCatastral, Nit, Nombre
from propiedades.modulos.ingestion.dominio.entidades import Propiedad
from propiedades.modulos.ingestion.dominio.fabricas import FabricaIngestion
from .dto import Propiedad as PropiedadDTO
from .dto import EventosPropiedad
from .mapeadores import MapeadorPropiedad, MapadeadorEventosPropiedad
from uuid import UUID
from pulsar.schema import *

class RepositorioPropiedadSQLAlchemy(RepositorioPropiedad):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_ingestion.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosPropiedadSQLAlchemy(RepositorioEventosPropiedad):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(propiedad_dto, MapadeadorEventosPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError

    def agregar(self, evento):
        propiedad_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosPropiedad())

        parser_payload = JsonSchema(propiedad_evento.data.__class__)
        json_str = parser_payload.encode(propiedad_evento.data)

        evento_dto = EventosPropiedad()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_propiedad)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(propiedad_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(propiedad_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, propiedad: Propiedad):
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        raise NotImplementedError