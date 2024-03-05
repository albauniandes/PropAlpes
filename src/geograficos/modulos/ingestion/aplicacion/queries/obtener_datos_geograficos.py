from geograficos.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from geograficos.seedwork.aplicacion.queries import ejecutar_query as query
from geograficos.modulos.ingestion.infraestructura.repositorios import RepositorioDatosGeograficos
from dataclasses import dataclass
from .base import DatosGeograficosQueryBaseHandler
from geograficos.modulos.ingestion.aplicacion.mapeadores import MapeadorDatosGeograficos
import uuid


@dataclass
class ObtenerDatosGeograficos(Query):
    id: str


class ObtenerDatosGeograficosHandler(DatosGeograficosQueryBaseHandler):

    def handle(self, query: ObtenerDatosGeograficos) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDatosGeograficos.__class__)
        datos_geograficos = self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorDatosGeograficos())
        return QueryResultado(resultado=datos_geograficos)


@query.register(ObtenerDatosGeograficos)
def ejecutar_query_obtener_datos_geograficos(query: ObtenerDatosGeograficos):
    handler = ObtenerDatosGeograficosHandler()
    # breakpoint()
    return handler.handle(query)
