from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from companias.modulos.ingestion.dominio.eventos import CompaniaCreada, CompaniaRechazada, CompaniaAprobada, CompaniaPagada

dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_creada, signal=f'{CompaniaCreada.__name__}Integracion')
dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_cancelada, signal=f'{CompaniaRechazada.__name__}Integracion')
dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_pagada, signal=f'{CompaniaPagada.__name__}Integracion')
dispatcher.connect(HandlerCompaniaIntegracion.handle_compania_aprobada, signal=f'{CompaniaAprobada.__name__}Integracion')