from pydispatch import dispatcher

from .handlers import HandlerAuditoriaPropiedadIntegracion

from auditoria.modulos.propiedades.dominio.eventos import AuditoriaPropiedadCreada

dispatcher.connect(HandlerAuditoriaPropiedadIntegracion.handle_auditoria_propiedad_creada, signal=f'{AuditoriaPropiedadCreada.__name__}Integracion')
