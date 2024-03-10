from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from propiedades.modulos.ingestion.dominio.eventos import PropiedadCreada, PropiedadRechazada, PropiedadAprobada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada, signal=f'{PropiedadCreada.__name__}Integracion')
dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_cancelada, signal=f'{PropiedadRechazada.__name__}Integracion')
dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_aprobada, signal=f'{PropiedadAprobada.__name__}Integracion')