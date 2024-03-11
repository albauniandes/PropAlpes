from auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from auditoria.seedwork.aplicacion.queries import ejecutar_query as query
from auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioAuditoriaPropiedads
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from auditoria.modulos.propiedades.aplicacion.mapeadores import MapeadorAuditoriaPropiedad
import uuid


@dataclass
class ObtenerAuditoriaPropiedad(Query):
    id: str


class ObtenerAuditoriaPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerAuditoriaPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoriaPropiedads.__class__)
        compania = self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorAuditoriaPropiedad())
        return QueryResultado(resultado=compania)


@query.register(ObtenerAuditoriaPropiedad)
def ejecutar_query_obtener_compania(query: ObtenerAuditoriaPropiedad):
    handler = ObtenerAuditoriaPropiedadHandler()
    # breakpoint()
    return handler.handle(query)
