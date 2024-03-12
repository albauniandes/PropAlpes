from propiedades.seedwork.aplicacion.comandos import Comando, ComandoHandler
from propiedades.seedwork.aplicacion.comandos import ejecutar_comando as comando
from .base import EliminarPropiedadBaseHandler

class RechazarPropiedad(Comando):
    propiedad_id: str

class RechazarPropiedadHandler(EliminarPropiedadBaseHandler):
    def handle(self, comando: RechazarPropiedad):
        propiedad_id = comando.propiedad_id
        
        repositorio = self.fabrica_repositorio
        repositorio_alchemy = repositorio.eliminar_objeto()
        repositorio_alchemy.eliminar(propiedad_id)

        from propiedades.config.db import db
        db.session.commit()

@comando.register(RechazarPropiedad)
def ejecutar_comando_rechazar_propiedad(comando: RechazarPropiedad):
    handler = RechazarPropiedadHandler()
    handler.handle(comando)