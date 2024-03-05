from geograficos.seedwork.aplicacion.servicios import Servicio
from geograficos.modulos.ingestion.dominio.entidades import DatosGeograficos
from geograficos.modulos.ingestion.dominio.fabricas import FabricaIngestion
from geograficos.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from geograficos.modulos.ingestion.infraestructura.repositorios import RepositorioDatosGeograficos
from geograficos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorDatosGeograficos

from .dto import DatosGeograficosDTO

import asyncio

class ServicioDatosGeograficos(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion       
    
    def crear_datos_geograficos(self, datos_geograficos_dto: DatosGeograficosDTO) -> DatosGeograficosDTO:
        datos_geograficos: DatosGeograficos = self.fabrica_ingestion.crear_objeto(datos_geograficos_dto, MapeadorDatosGeograficos())
        datos_geograficos.crear_datos_geograficos(datos_geograficos)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDatosGeograficos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, datos_geograficos)
        # UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_ingestion.crear_objeto(datos_geograficos, MapeadorDatosGeograficos())

    def obtener_datos_geograficos_por_id(self, id) -> DatosGeograficosDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDatosGeograficos.__class__)
        return self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(id), MapeadorDatosGeograficos())

