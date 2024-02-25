'''Comando para iniciar validación de datos con la compañía y solicitud de autorización para su uso'''

from companias.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class ValidarCompania(Comando):
    id_compania: uuid.UUID

class ValidarCompaniaHandler(ComandoHandler):
    ...