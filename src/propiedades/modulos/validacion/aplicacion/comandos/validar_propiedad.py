'''Comando para iniciar validación de datos con la compañía y solicitud de autorización para su uso'''

from propiedades.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class ValidarPropiedad(Comando):
    id_propiedad: uuid.UUID

class ValidarPropiedadHandler(ComandoHandler):
    ...