from auditoria_test.seedwork.aplicacion.queries import QueryHandler
from auditoria_test.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from auditoria_test.modulos.companias.dominio.fabricas import FabricaAuditoriaCompania

class CompaniaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria_companias: FabricaAuditoriaCompania = FabricaAuditoriaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria_companias(self):
        return self._fabrica_auditoria_companias