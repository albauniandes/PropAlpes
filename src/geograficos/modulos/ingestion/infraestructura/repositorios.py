""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from geograficos.config.db import db
from geograficos.modulos.ingestion.dominio.repositorios import RepositorioDatosGeograficos, RepositorioEventosDatosGeograficos
from geograficos.modulos.ingestion.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from geograficos.modulos.ingestion.dominio.fabricas import FabricaIngestion
from .dto import DatosGeograficos as DatosGeograficosDTO
from .dto import EventosDatosGeograficos
from .mapeadores import MapeadorDatosGeograficos, MapadeadorEventosDatosGeograficos
from uuid import UUID
from pulsar.schema import *

class RepositorioCompaniasSQLAlchemy(RepositorioDatosGeograficos):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> DatosGeograficos:
        datos_geograficos_dto = db.session.query(DatosGeograficosDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(datos_geograficos_dto, MapeadorDatosGeograficos())

    def obtener_todos(self) -> list[DatosGeograficos]:
        # TODO
        raise NotImplementedError

    def agregar(self, datos_geograficos: DatosGeograficos):
        datos_geograficos_dto = self.fabrica_ingestion.crear_objeto(datos_geograficos, MapeadorDatosGeograficos())
        db.session.add(datos_geograficos_dto)

    def actualizar(self, datos_geograficos: DatosGeograficos):
        # TODO
        raise NotImplementedError

    def eliminar(self, datos_geograficos_id: UUID):
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