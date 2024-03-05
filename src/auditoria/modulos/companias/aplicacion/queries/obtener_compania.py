from auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from auditoria.seedwork.aplicacion.queries import ejecutar_query as query
from auditoria.modulos.companias.infraestructura.repositorios import Repo
from dataclasses import dataclass
from .base import CompaniaQueryBaseHandler
from companias.modulos.ingestion.aplicacion.mapeadores import MapeadorCompania
import uuid


@dataclass
class ObtenerAuditoriaCompania(Query):
    id: str


class ObtenerAuditoriaCompaniaHandler(CompaniaQueryBaseHandler):

    def handle(self, query: ObtenerAuditoriaCompania) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        compania = self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCompania())
        return QueryResultado(resultado=compania)


@query.register(ObtenerAuditoriaCompania)
def ejecutar_query_obtener_compania(query: ObtenerAuditoriaCompania):
    handler = ObtenerAuditoriaCompaniaHandler()
    # breakpoint()
    return handler.handle(query)
