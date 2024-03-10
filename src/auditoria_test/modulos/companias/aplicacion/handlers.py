from auditoria_test.modulos.companias.dominio.eventos import AuditoriaCompaniaCreada
from auditoria_test.seedwork.aplicacion.handlers import Handler
from auditoria_test.modulos.companias.infraestructura.despachadores import Despachador

class HandlerAuditoriaCompaniaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria-compania')


    