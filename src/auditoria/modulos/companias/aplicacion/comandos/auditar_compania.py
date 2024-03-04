from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.modulos.companias.aplicacion.dto import AuditoriaCompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando

from auditoria.modulos.companias.dominio.entidades import Compania
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from auditoria.modulos.companias.aplicacion.mapeadores import MapeadorCompania
from auditoria.modulos.companias.infraestructura.repositorios import RepositorioCompanias, RepositorioEventosCompanias

from pydispatch import dispatcher

@dataclass
class CrearAuditoriaCompania(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    email: str
    identificacion: str
    motivo_auditoria: str


class CrearAuditoriaCompaniaHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: CrearAuditoriaCompania):
        auditoria_compania_dto = AuditoriaCompaniaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   nombre=comando.nombre
            ,   email=comando.email
            ,   identificacion=comando.identificacion
            ,   motivo_auditoria=comando.motivo_auditoria)
        #breakpoint()
        auditoria_compania: AuditoriaCompania = self.fabrica_ingestion.crear_objeto(auditoria_compania_dto, MapeadorCompania())
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
    