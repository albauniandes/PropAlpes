from companias.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerCompaniasNoPagadas(Query):
    ...

class ObtenerCompaniasNoPagadasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...