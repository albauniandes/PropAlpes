

from propiedades.modulos.ingestion.dominio.eventos import PropiedadCreada
from propiedades.seedwork.aplicacion.handlers import Handler

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        #breakpoint()
        print('================ PROPIEDAD CREADA ===========')
        

