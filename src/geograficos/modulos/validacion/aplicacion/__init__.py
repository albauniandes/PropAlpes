from pydispatch import dispatcher
from .handlers import HandlerDatosGeograficosDominio

dispatcher.connect(HandlerDatosGeograficosDominio.handle_datos_geograficos_creada, signal='DatosGeograficosCreadaDominio')