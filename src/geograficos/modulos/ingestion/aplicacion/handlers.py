from geograficos.modulos.ingestion.dominio.eventos import DatosGeograficosCreados, DatosGeograficosRechazados, DatosGeograficosAprobados
from geograficos.seedwork.aplicacion.handlers import Handler
from geograficos.modulos.ingestion.infraestructura.despachadores import Despachador

class HandlerDatosGeograficosIntegracion(Handler):

    @staticmethod
    def handle_datos_geograficos_creados(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-datos-geograficos')

    @staticmethod
    def handle_datos_geograficos_cancelados(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-datos-geograficos')

    @staticmethod
    def handle_datos_geograficos_aprobados(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-datos-geograficos')

    @staticmethod
    def handle_datos_geograficos_pagados(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-datos-geograficos')


    