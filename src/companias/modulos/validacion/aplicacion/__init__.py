from pydispatch import dispatcher
from .handlers import HandlerCompaniaDominio

dispatcher.connect(HandlerCompaniaDominio.handle_compania_creada, signal='CompaniaCreadaDominio')
