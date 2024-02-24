from companias.modulos.ingestion.dominio.eventos import CompaniaCreada, CompaniaRechazada, CompaniaAprobada, CompaniaPagada
from companias.seedwork.aplicacion.handlers import Handler
from companias.modulos.ingestion.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')

    @staticmethod
    def handle_compania_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')

    @staticmethod
    def handle_compania_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')

    @staticmethod
    def handle_compania_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')


    