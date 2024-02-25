from companias.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerCompaniasRechazadas(Query):
    ...

class ObtenerCompaniasRechachazadasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...