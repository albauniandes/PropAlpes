from auditoria.modulos.sagas.aplicacion.comandos.base import RechazarPropiedadBaseHandler
from auditoria.modulos.sagas.infraestructura.despachadores import DespachadorPropiedades
from auditoria.seedwork.aplicacion.comandos import Comando, ComandoHandler
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando

class CrearPropiedad():
    ...

class EliminarPropiedad():
    ...

class RechazarPropiedad(Comando):
    propiedad_id: str

class RechazarPropiedadHandler(RechazarPropiedadBaseHandler):
    def handle(self, comando: RechazarPropiedad):
        propiedad_id = comando.propiedad_id
        
        despachador = DespachadorPropiedades()
        despachador.publicar_comando_rechazar_propiedad(propiedad_id)

@comando.register(RechazarPropiedad)
def ejecutar_comando_rechazar_propiedad(comando: RechazarPropiedad):
    handler = RechazarPropiedadHandler()
    handler.handle(comando)