'''Comando para iniciar validación de datos con la compañía y solicitud de autorización para su uso'''

from geograficos.seedwork.aplicacion.comandos import Comando, ComandoHandler    

class ValidarDatosGeograficos(Comando):
    id_datos_geograficos: uuid.UUID

class ValidarDatosGeograficosHandler(ComandoHandler):
    ...