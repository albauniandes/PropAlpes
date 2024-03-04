from companias.seedwork.aplicacion.comandos import Comando
from companias.modulos.ingestion.aplicacion.dto import CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from companias.seedwork.aplicacion.comandos import ejecutar_comando as comando

from companias.modulos.ingestion.dominio.entidades import Compania
from companias.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from companias.modulos.ingestion.aplicacion.mapeadores import MapeadorCompania
from companias.modulos.ingestion.infraestructura.repositorios import RepositorioCompanias, RepositorioEventosCompanias

from pydispatch import dispatcher

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
        #breakpoint()
        compania: Compania = self.fabrica_ingestion.crear_objeto(compania_dto, MapeadorCompania())
        compania.crear_compania(compania)
        #breakpoint()
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosCompanias)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania, repositorio_eventos_func=repositorio_eventos.agregar)

        repositorio.agregar(compania)

        for evento in compania.eventos:
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        #UnidadTrabajoPuerto.commit()
        from companias.config.db import db
        db.session.commit()

@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
    