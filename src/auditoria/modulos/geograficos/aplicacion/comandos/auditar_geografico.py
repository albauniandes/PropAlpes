from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.modulos.geograficos.aplicacion.dto import AuditoriaGeograficoDTO
from .base import CrearAuditoriaPropiedadBaseHandler
from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando

from auditoria.modulos.geograficos.dominio.entidades import AuditoriaGeografico
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from auditoria.modulos.propiedades.aplicacion.mapeadores import MapeadorAuditoriaPropiedad
from auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioAuditoriaPropiedads, RepositorioEventosAuditoriaPropiedads

from pydispatch import dispatcher

@dataclass
class CrearAuditoriaGeografico(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    latitud: str
    longitud: str
    identificacion: str
    motivo_auditoria: str


class CrearAuditoriaGeograficoHandler(CrearAuditoriaPropiedadBaseHandler):
    
    def handle(self, comando: CrearAuditoriaGeografico):
        auditoria_geografico_dto = AuditoriaGeograficoDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   latitud=comando.latitud
            ,   longitud=comando.longitud
            ,   identificacion=comando.identificacion
            ,   motivo_auditoria=comando.motivo_auditoria)
        #breakpoint()
        auditoria_compania: AuditoriaPropiedad = self.fabrica_ingestion.crear_objeto(auditoria_geografico_dto, MapeadorAuditoriaGeografico())
        auditoria_compania.crear_auditoria_propiedad(auditoria_compania)
        #breakpoint()
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoriaPropiedads.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosAuditoriaPropiedads)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania, repositorio_eventos_func=repositorio_eventos.agregar)

        repositorio.agregar(auditoria_compania)

        for evento in auditoria_compania.eventos:
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        #UnidadTrabajoPuerto.commit()
        from companias.config.db import db
        db.session.commit()

@comando.register(CrearAuditoriaGeografico)
def ejecutar_comando_crear_compania(comando: CrearAuditoriaGeografico):
    handler = CrearAuditoriaGeograficoHandler()
    handler.handle(comando)
    