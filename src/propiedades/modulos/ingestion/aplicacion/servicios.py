from propiedades.seedwork.aplicacion.servicios import Servicio
from propiedades.modulos.ingestion.dominio.entidades import Propiedad
from propiedades.modulos.ingestion.dominio.fabricas import FabricaIngestion
from propiedades.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.ingestion.infraestructura.repositorios import RepositorioPropiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

import asyncio

class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion       
    
    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_ingestion.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedad.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        # UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_ingestion.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedad.__class__)
        return self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

