from geograficos.seedwork.aplicacion.comandos import Comando, ComandoHandler
from geograficos.seedwork.aplicacion.comandos import ejecutar_comando as comando
from .base import EliminarDatosGeograficosBaseHandler

class RechazarDatosGeograficos(Comando):
    geograficos_id: str

class RechazarDatosGeograficosHandler(EliminarDatosGeograficosBaseHandler):
    def handle(self, comando: RechazarDatosGeograficos):
        geograficos_id = comando.geograficos_id
        
        repositorio = self.fabrica_repositorio
        repositorio_alchemy = repositorio.eliminar_objeto()
        repositorio_alchemy.eliminar(geograficos_id)

        from geograficos.config.db import db
        db.session.commit()

@comando.register(RechazarDatosGeograficos)
def ejecutar_comando_rechazar_datos_geograficos(comando: RechazarDatosGeograficos):
    handler = RechazarDatosGeograficosHandler()
    handler.handle(comando)