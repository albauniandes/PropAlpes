from pydispatch import dispatcher

from .handlers import HandlerAuditoriaCompaniaIntegracion

from auditoria.modulos.companias.dominio.eventos import AuditoriaCompaniaCreada

dispatcher.connect(HandlerAuditoriaCompaniaIntegracion.handle_auditoria_compania_creada, signal=f'{AuditoriaCompaniaCreada.__name__}Integracion')
