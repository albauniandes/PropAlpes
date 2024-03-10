from propiedades.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedades.seedwork.aplicacion.queries import ejecutar_query as query
from propiedades.modulos.ingestion.infraestructura.repositorios import RepositorioPropiedad
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from propiedades.modulos.ingestion.aplicacion.mapeadores import MapeadorPropiedad
import uuid


@dataclass
class ObtenerPropiedad(Query):
    id: str


class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedad.__class__)
        propiedad = self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=propiedad)


@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    # breakpoint()
    return handler.handle(query)
