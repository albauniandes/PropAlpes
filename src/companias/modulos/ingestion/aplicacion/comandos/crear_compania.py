from companias.seedwork.aplicacion.comandos import Comando
from companias.modulos.ingestion.aplicacion.dto import ItinerarioDTO, CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from companias.seedwork.aplicacion.comandos import ejecutar_commando as comando

from companias.modulos.ingestion.dominio.entidades import Compania
from companias.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from companias.modulos.ingestion.aplicacion.mapeadores import MapeadorCompania
from companias.modulos.ingestion.infraestructura.repositorios import RepositorioCompanias

@dataclass
class CrearCompania(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    email: str
    identificacion: str


class CrearCompaniaHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: CrearCompania):
        compania_dto = CompaniaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   nombre=comando.nombre
            ,   email=comando.email
            ,   identificacion=comando.identificacion)

        compania: Compania = self.fabrica_ingestion.crear_objeto(compania_dto, MapeadorCompania())
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
    