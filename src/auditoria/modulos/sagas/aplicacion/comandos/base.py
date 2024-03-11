from auditoria.modulos.geograficos.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.sagas.dominio.fabricas import FabricaIngestion
from auditoria.seedwork.aplicacion.comandos import ComandoHandler


class RechazarDatosGeograficosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion    
    

class EliminarDatosGeograficosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion   
    