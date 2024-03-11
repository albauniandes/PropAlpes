from auditoria.modulos.sagas.aplicacion.comandos.base import RechazarDatosGeograficosBaseHandler
from auditoria.modulos.sagas.infraestructura.despachadores import Despachador
from auditoria.seedwork.aplicacion.comandos import Comando, ComandoHandler
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando

class CrearGeografico():
    ...

class EliminarGeografico():
    ...

class RechazarDatosGeograficos(Comando):
    geograficos_id: str

class RechazarDatosGeograficosHandler(RechazarDatosGeograficosBaseHandler):
    def handle(self, comando: RechazarDatosGeograficos):
        geograficos_id = comando.geograficos_id
        
        despachador = Despachador()
        despachador.publicar_comando_rechazar_geograficos(geograficos_id)

@comando.register(RechazarDatosGeograficos)
def ejecutar_comando_rechazar_datos_geograficos(comando: RechazarDatosGeograficos):
    handler = RechazarDatosGeograficosHandler()
    handler.handle(comando)



