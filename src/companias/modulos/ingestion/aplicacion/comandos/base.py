from companias.seedwork.aplicacion.comandos import ComandoHandler
from companias.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from companias.modulos.ingestion.dominio.fabricas import FabricaVuelos

class CrearCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion    
    