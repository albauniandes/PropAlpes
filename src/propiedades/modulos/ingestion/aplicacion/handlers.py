from propiedades.modulos.ingestion.dominio.eventos import PropiedadCreada, PropiedadRechazada, PropiedadAprobada
from propiedades.seedwork.aplicacion.handlers import Handler
from propiedades.modulos.ingestion.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'topic-eventos-propiedad')

    @staticmethod
    def handle_propiedad_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'topic-eventos-propiedad')

    @staticmethod
    def handle_propiedad_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'topic-eventos-propiedad')

    @staticmethod
    def handle_propiedad_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'topic-eventos-propiedad')


    