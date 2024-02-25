from companias.seedwork.aplicacion.servicios import Servicio
from companias.modulos.ingestion.dominio.entidades import Compania
from companias.modulos.ingestion.dominio.fabricas import FabricaIngestion
from companias.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from companias.modulos.ingestion.infraestructura.repositorios import RepositorioCompanias
from companias.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorCompania

from .dto import CompaniaDTO

import asyncio

class ServicioCreacionEmpresa(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion       
    
    def crear_compania(self, compania_dto: CompaniaDTO) -> CompaniaDTO:
        compania: Compania = self.fabrica_ingestion.crear_objeto(compania_dto, MapeadorCompania())
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        # UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_ingestion.crear_objeto(compania, MapeadorCompania())

    def obtener_compania_por_id(self, id) -> CompaniaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        return self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(id), MapeadorCompania())

