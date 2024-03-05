

from geograficos.modulos.ingestion.dominio.eventos import DatosGeograficosCreados
from geograficos.seedwork.aplicacion.handlers import Handler

class HandlerDatosGeograficosDominio(Handler):

    @staticmethod
    def handle_datos_geograficos_creada(evento):
        #breakpoint()
        print('================ DATOS GEOGRAFICOS CREADOS ===========')
        

