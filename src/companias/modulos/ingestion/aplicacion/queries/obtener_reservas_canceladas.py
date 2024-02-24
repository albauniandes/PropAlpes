from companias.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerCompaniasCanceladas(Query):
    ...

class ObtenerCompaniasCanceladasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...