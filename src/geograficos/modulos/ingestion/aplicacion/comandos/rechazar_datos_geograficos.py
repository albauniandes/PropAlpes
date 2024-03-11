from geograficos.seedwork.aplicacion.comandos import Comando, ComandoHandler
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando as comando
from .base import EliminarDatosGeograficosBaseHandler

class RechazarDatosGeograficos(Comando):
    id_geograficos: str

class RechazarDatosGeograficosHandler(EliminarDatosGeograficosBaseHandler):
    def handle(self, comando: RechazarDatosGeograficos):
        id_geograficos = comando.id_geograficos
        
        repositorio = self.fabrica_repositorio()
        repositorio.eliminar(id_geograficos)

        from geograficos.config.db import db
        db.session.commit()

@comando.register(RechazarDatosGeograficos)
def ejecutar_comando_rechazar_datos_geograficos(comando: RechazarDatosGeograficos):
    handler = RechazarDatosGeograficosHandler()
    handler.handle(comando)