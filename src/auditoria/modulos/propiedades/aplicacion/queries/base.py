from auditoria.seedwork.aplicacion.queries import QueryHandler
from auditoria.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.propiedades.dominio.fabricas import FabricaAuditoriaPropiedad

class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria_propiedades: FabricaAuditoriaPropiedad = FabricaAuditoriaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria_propiedades(self):
        return self._fabrica_auditoria_propiedades