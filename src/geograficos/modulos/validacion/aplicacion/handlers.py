

from companias.modulos.ingestion.dominio.eventos import CompaniaCreada
from companias.seedwork.aplicacion.handlers import Handler

class HandlerCompaniaDominio(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        #breakpoint()
        print('================ COMPAÑIA CREADA ===========')
        

