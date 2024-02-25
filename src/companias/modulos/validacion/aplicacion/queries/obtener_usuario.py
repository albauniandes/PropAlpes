from companias.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerAutorizacion(Query):
    listing_id: uuid.UUID

class ObtenerAutorizacionHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...