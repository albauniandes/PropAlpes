from auditoria.seedwork.aplicacion.comandos import ComandoHandler
from auditoria.modulos.geograficos.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.geograficos.dominio.fabricas import FabricaAuditoriaPropiedad

class CrearAuditoriaPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria_propiedad: FabricaAuditoriaPropiedad = FabricaAuditoriaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria_propiedad(self):
        return self._fabrica_auditoria_propiedad


class EliminarAuditoriaPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria_propiedad: FabricaAuditoriaPropiedad = FabricaAuditoriaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_auditoria_propiedad(self):
        return self._fabrica_auditoria_propiedad