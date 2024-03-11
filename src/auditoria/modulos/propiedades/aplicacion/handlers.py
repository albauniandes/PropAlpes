from auditoria.modulos.propiedades.dominio.eventos import AuditoriaPropiedadCreada
from auditoria.seedwork.aplicacion.handlers import Handler
from auditoria.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerAuditoriaPropiedadIntegracion(Handler):

    @staticmethod
    def handle_auditoria_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria-propiedad')


    