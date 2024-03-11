""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de ingestión"""

from auditoria.config.db import db

from auditoria.modulos.sagas.dominio.repositorios import RepositorioDatosGeograficos, RepositorioEventosDatosGeograficos
from auditoria.modulos.sagas.dominio.objetos_valor import EstadoDatosGeograficos, NombrePropiedad, Latitud, Longitud
from auditoria.modulos.sagas.dominio.entidades import DatosGeograficos
from auditoria.modulos.sagas.dominio.fabricas import FabricaIngestion

from .dto import DatosGeograficos as DatosGeograficosDTO
from .dto import EventosDatosGeograficos
from .mapeadores import MapeadorDatosGeograficos, MapadeadorEventosDatosGeograficos
from uuid import UUID
from pulsar.schema import *

class RepositorioDatosGeograficosSQLAlchemy(RepositorioDatosGeograficos):

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


class RepositorioEventosDatosGeograficosSQLAlchemy(RepositorioEventosDatosGeograficos):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> DatosGeograficos:
        datos_geograficos_dto = db.session.query(DatosGeograficosDTO).filter_by(id=str(id)).one()
        return self.fabrica_ingestion.crear_objeto(datos_geograficos_dto, MapadeadorEventosDatosGeograficos())

    def obtener_todos(self) -> list[DatosGeograficos]:
        raise NotImplementedError

    def agregar(self, evento):
        datos_geograficos_evento = self.fabrica_ingestion.crear_objeto(evento, MapadeadorEventosDatosGeograficos())

        parser_payload = JsonSchema(datos_geograficos_evento.data.__class__)
        json_str = parser_payload.encode(datos_geograficos_evento.data)

        evento_dto = EventosDatosGeograficos()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_datos_geograficos)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(datos_geograficos_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(datos_geograficos_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, datos_geograficos: DatosGeograficos):
        raise NotImplementedError

    def eliminar(self, datos_geograficos_id: UUID):
        raise NotImplementedError