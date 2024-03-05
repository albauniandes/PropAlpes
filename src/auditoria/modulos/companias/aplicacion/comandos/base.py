from auditoria.seedwork.aplicacion.comandos import ComandoHandler
from auditoria.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.companias.dominio.fabricas import FabricaAuditoriaCompania

class CrearAuditoriaCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria_companias: FabricaAuditoriaCompania = FabricaAuditoriaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria_compania(self):
        return self._fabrica_auditoria_companias
