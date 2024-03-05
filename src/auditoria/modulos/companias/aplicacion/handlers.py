from auditoria.modulos.companias.dominio.eventos import AuditoriaCompaniaCreada
from auditoria.seedwork.aplicacion.handlers import Handler
from auditoria.modulos.companias.infraestructura.despachadores import Despachador

class HandlerAuditoriaCompaniaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria-compania')


    