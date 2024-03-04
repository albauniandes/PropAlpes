from companias.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery

class ObtenerTodasCompaniasPagadas(Query):
    ...

class ObtenerTodasCompaniasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...